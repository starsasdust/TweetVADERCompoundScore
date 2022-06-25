# -*- coding: utf-8 -*-
"""
This py file transfer all monthly python dict into a csv file with some added data
a. the percentage of positive/neutral/negative tweets of that month
b. convert date string into date type data
Created on Thu Jun 23 16:28:54 2022

@author: Xu Du
"""

Rlist=[{'Date':'1-2019','pos': 79616, 'neu': 466535, 'neg': 54724, 'avg': 0.027013368337837518, 'std': 0.24795680997787883, 'Pavg': 0.508465181621746, 'Pstd': 0.21465945677119594, 'Navg': -0.44327771909937363, 'Nstd': 0.20833573817137022},\
{'Date':'2-2019','pos': 78698, 'neu': 457832, 'neg': 55562, 'avg': 0.026496104490514726, 'std': 0.25177273108286113, 'Pavg': 0.5148866629393236, 'Pstd': 0.21493787742571335, 'Navg': -0.44710017817923303, 'Nstd': 0.20525668152401827},]
import csv
from datetime import datetime # Import the packages
TotTwt=0                      # Define total tweets
MonthTwt=0                    # Define tweets month average
for i in Rlist:               # For every month data in the list
    TotTwt+=i['pos']          # Add the all counters to total tweets
    TotTwt+=i['neu']
    TotTwt+=i['neg']
    i['pos%']=i['pos']/(i['pos']+i['neu']+i['neg'])   # Caculate the percentage of each types of tweets
    i['neu%']=i['neu']/(i['pos']+i['neu']+i['neg'])
    i['neg%']=i['neg']/(i['pos']+i['neu']+i['neg'])
    k=str(i['Date'])                                  # Convert date string to date data
    i['Date']=datetime.strptime(k,"%m-%Y")            
MonthTwt=int(TotTwt/12)                               # Caculate the tweets month average

# Define the header of CSV file
TweetPolarVader = ['Date','pos', 'neu', 'neg', 'avg', 'std', 'Pavg', 'Pstd', 'Navg', 'Nstd', 'pos%', 'neu%', 'neg%']
# Convert the list of dict into CSV file
with open('result.csv', 'w') as csvfile:
    CSV = csv.DictWriter(csvfile, fieldnames = TweetPolarVader) # Define the csv writer
    CSV.writeheader()                                           # Write the header of csv   
    CSV.writerows(Rlist)                                        # Write the data into csv 
    
    
    
    
