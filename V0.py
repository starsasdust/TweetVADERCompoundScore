import os
import json
from langdetect import detect
from datetime import datetime
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def twJs(jsfile):                 # Define the function to covert json file to tweet list
    twt_list=[]                   # Defien the list of tweet
    tjs = open(jsfile, 'r')       # Open the json file
    tj = tjs.read().split('\n')   # split the json file
    for twt in tj:                # 
        tweet={}
        try:
            twt_obj= json.loads(twt)
            if "extended_tweet" in twt_obj:
                tweet["text"]=twt_obj["extended_tweet"]["full_text"]
            elif "text" in twt_obj:
                tweet["text"]=twt_obj["text"]
            else:
                continue
            if "created_at" in twt_obj:
                i=twt_obj["created_at"]
                k=i[4:7]+" "+i[(len(i)-4):]
                tweet['time']=datetime.strptime(k,'%b %Y')
            else:
                continue
            twt_list.append(tweet)
        except json.decoder.JSONDecodeError:
            continue
    return twt_list

def EnFtr(twt_list):
    English_twt=[]
    for i in twt_list:
        try:
            lang=detect(i["text"])
        except:
            continue
        if lang=="en":
            English_twt.append(i)
    return English_twt

def SentiList(twt_list):
    SIA = SentimentIntensityAnalyzer()
    Score_list=[]
    for i in twt_list:
        twtScore={}
        try:
            Scores = SIA.polarity_scores(i["text"])
        except:
            continue
        twtScore["date"]=i["time"]
        twtScore["PolScore"]=Scores['compound']
        Score_list.append(twtScore)
    return Score_list

def openfiledir(path):
    outputlist=[]
    os.chdir(path)
    for root, dirs, files in os.walk(path):
     for file in files:
        if file.endswith(".json"):
            twt_list=twJs(os.path.join(root, file))
            outputlist.extend(twt_list)
    return outputlist

listJan2020=openfiledir(r'path')



        

