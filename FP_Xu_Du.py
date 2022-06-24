# -*- coding: utf-8 -*-
"""
TweetJsonVaderPolarScore
This py file has the following functions.
1. Flattering the JSON format tweets to python list with each tweet as a dictionary type
   a. Due to the scale of this final project. only text of every tweet is extracted
   b. For extended tweets (longer than 140), the full text is the text for tweets
   c. In this project, the retweeted tweets' text is not included
2. Utilize the VADER classifier from the NLTK to assign polarity classification score to the text of tweet
   a. only compound score
   b. compound score is in the range [-1,1], where -1 is the most negative and +1 as the most positive
   c. (-0.05, 0.05) is the neutral score range
3. A function to loop the folder for each JSON file
4. A function for final output
   a. the final output is a python dictionary of the analyzing result in one month
   b. The one-month scale is due to the operating time and RAM consumption of the code,
      even with reduced tweets data size, the operation took more than 2Gb ram to run.
      If we do it for multiple months, we may need a memory management setting.
   c. The keys of the dictionary are:
      pos: number of tweets that has a positive compound score
      neu: number of tweets that has a neutral compound score
      neg: number of tweets that has a negative compound score
      avg: the average compound score of all tweets
      std: the standard division of all compound score
      P/Navg: The average compound score of all Positive/Negative tweets
      P/Nstd: The standard division of all Positive/Negative tweets
Created on Thu Jun 20 14:23:15 2022


@author: Xu Du
"""
# import all necessay py packages
import os
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import statistics

def twJs(jsfile):                 # Define the function to covert json file(the parameter) to tweet list
    twt_list=[]                   # Defien the list of tweet
    tjs = open(jsfile, 'r')       # Open the json file
    tj = tjs.read().split('\n')   # split the json file
    for twt in tj:                # Define a for loop to go through every tweet object
        try:                      # Define a try-except for error(empty/deleted tweets)
            twt_obj= json.loads(twt)                         # Use json.load to extract tweet object
            if "extended_tweet" in twt_obj:                  # Define if statement for extended tweet 
                tweet=twt_obj["extended_tweet"]["full_text"] # Define the text for the tweet
            elif "text" in twt_obj:                          # if it is a regular tweet
                tweet=twt_obj["text"]                        # Define the text for the tweet
            else:
                continue                                     # Skip tweets without text
            twt_list.append(tweet)                           # Add the text into the list
        except json.decoder.JSONDecodeError:                 # Skip empty or deleted tweet
            continue                                         
    return twt_list                                          # Output the list of tweet text

def SentiList(twt_list):                                     # Define the function to give VADER score(tweet text list as the parameter)
    SIA = SentimentIntensityAnalyzer()                       # Define the new SentimentIntensityAnalyzer()
    Score_list=[]                                            # Define the new list of scores
    for i in twt_list:                                       # Define a for loop to go through every text
        try:                                                 # Define a try-except for text VADER can't handel  
            Scores = SIA.polarity_scores(i)                  # The compound score is the result of SentimentIntensityAnalyzer() use text as the parameter
        except:
            continue                                         # Skip the text which can not be scored
        twtScore=Scores['compound']                          # The original result of VADER is a python dictionary with all types of score, we only need the "compound"
        Score_list.append(twtScore)                          # Add the compound score to the list
    return Score_list                                        # Output the score list

def openfiledir(path):                                       # Define the function to open every JSON file in the folder path
    outputlist=[]                                            # Define the output list
    os.chdir(path)                                           # Define the folder path
    for root, dirs, files in os.walk(path):                  # Utlize os.walk to go through the folder and subfoler
     for file in files:                                      # Define for loop to open ever file
        if file.endswith(".json"):                           # Define if statement to only open JSON file
            twt_list=twJs(os.path.join(root, file))          # Since the file only has file name, it need the full path, os.path.join will output the full path, we also called the JSON-Text function
            outputlist.extend(twt_list)                      # The JSON-text function return a list, so we need to use extend to add every item in list to the final output list
    return outputlist                                        # Output the final list

def monthresult(sentilist):                                  # Define the function to transfer the VADER score list into monthly data
    # Define the Score dictionary
    scoredict={'pos':0,'neu':0,'neg':0,'avg':0,'std':0,'Pavg':0,'Pstd':0,'Navg':0,'Nstd':0}
    itemN=0                       # Define the tweet number counter
    itemSum=0                     # Define the summary of all scores
    pSum=0                        # Define the summary of all Positive socres 
    plist=[]                      # Define the list of all positive score
    nSum=0                        # Define the summary of all Negative socres 
    nlist=[]                      # Define the list of all Negative score
    for i in sentilist:           # Define for loop for every score in the list
        itemN+=1                  # Add one to the tweet number counter
        itemSum+=i                # Add the score to the summary
        if i>=0.05:               # If it is a positive score
            scoredict['pos']+=1   # The counter of positive tweets add one
            pSum+=i               # Add the score to the Positive summary 
            plist.append(i)       # Add the score to the Positive list
        elif i <= -0.05:          # If it is a negative score
            scoredict['neg']+=1   # Add the score to the Negative summary 
            nSum+=i               # Add the score to the Negative summary 
            nlist.append(i)       # Add the score to the Negative list
        else:
            scoredict['neu']+=1   # Add one to the counter of neutral tweets
    scoredict['avg']=itemSum/itemN                  # Caculate the average score
    scoredict['std']=statistics.pstdev(sentilist)   # Caculate the standard division with statistics.pstdev()  
    scoredict['Pavg']=pSum/scoredict['pos']         # Caculate the average score of positive/negative tweets
    scoredict['Navg']=nSum/scoredict['neg']
    scoredict['Pstd']=statistics.pstdev(plist)      # Caculate the standard division of positive/negative tweets
    scoredict['Nstd']=statistics.pstdev(nlist)
    return scoredict                                # Output the final score dictionary

twt_list=openfiledir(r'folderpath') # Transfer JSON files to Tweets dict
sentilist=SentiList(twt_list)       # Calculate the polarity compoud score
Result=monthresult(sentilist)       # Output the final result dictionary 
            