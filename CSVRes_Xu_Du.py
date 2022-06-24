# -*- coding: utf-8 -*-
"""
This py file transfer all monthly python dict into a csv file with some added data
a. the percentage of positive/neutral/negative tweets of that month
b. convert date string into date type data
Created on Thu Jun 23 16:28:54 2022

@author: Xu Du
"""

Rlist=[{'Date':'1-2019','pos': 79616, 'neu': 466535, 'neg': 54724, 'avg': 0.027013368337837518, 'std': 0.24795680997787883, 'Pavg': 0.508465181621746, 'Pstd': 0.21465945677119594, 'Navg': -0.44327771909937363, 'Nstd': 0.20833573817137022},\
{'Date':'2-2019','pos': 78698, 'neu': 457832, 'neg': 55562, 'avg': 0.026496104490514726, 'std': 0.25177273108286113, 'Pavg': 0.5148866629393236, 'Pstd': 0.21493787742571335, 'Navg': -0.44710017817923303, 'Nstd': 0.20525668152401827},\
{'Date':'3-2019','pos': 85163, 'neu': 487492, 'neg': 59171, 'avg': 0.02665382114695982, 'std': 0.2530128288672593, 'Pavg': 0.5113135857120896, 'Pstd': 0.2154732581363476, 'Navg': -0.4514192949247663, 'Nstd': 0.21031532375590287},\
{'Date':'4-2019','pos': 92911, 'neu': 480944, 'neg': 59167, 'avg': 0.034036910723487905, 'std': 0.25951278950145673, 'Pavg': 0.5155572612500154, 'Pstd': 0.2152168241705624, 'Navg': -0.4455732570519683, 'Nstd': 0.21035851022589214},\
{'Date':'5-2019','pos': 78055, 'neu': 428532, 'neg': 53856, 'avg': 0.02839520040396294, 'std': 0.25769971993586976, 'Pavg': 0.5146711511113784, 'Pstd': 0.2161958972874991, 'Navg': -0.4505840482025266, 'Nstd': 0.21158271215495622},\
{'Date':'6-2019','pos': 76731, 'neu': 452341, 'neg': 51302, 'avg': 0.028253478791259567, 'std': 0.24782176351762064, 'Pavg': 0.5121009227039716, 'Pstd': 0.21330677323963948, 'Navg': -0.4464617480799203, 'Nstd': 0.21018559885893703},\
{'Date':'1-2020','pos': 94776, 'neu': 517232, 'neg': 67394, 'avg': 0.026212781534349444, 'std': 0.25579104575507416, 'Pavg': 0.505125647843291, 'Pstd': 0.21462737860187797, 'Navg': -0.4462846455172647, 'Nstd': 0.20910873876568223},\
{'Date':'2-2020','pos': 96284, 'neu': 502664, 'neg': 66204, 'avg': 0.030441276730739993, 'std': 0.26103866815454224, 'Pavg': 0.5154844325121074, 'Pstd': 0.21488346758228824, 'Navg': -0.4440113875293365, 'Nstd': 0.20771313229948168},\
{'Date':'3-2020','pos': 99223, 'neu': 565774, 'neg': 73935, 'avg': 0.023726409872626777, 'std': 0.2529144511418073, 'Pavg': 0.5063205597492239, 'Pstd': 0.21462338661074373, 'Navg': -0.44257919929653855, 'Nstd': 0.2077516277903451},\
{'Date':'4-2020','pos': 101621, 'neu': 585687, 'neg': 71711, 'avg': 0.026075541982483002, 'std': 0.24996778905337677, 'Pavg': 0.5073340854744148, 'Pstd': 0.2133478745617017, 'Navg': -0.4430707715690811, 'Nstd': 0.20729962968814758},\
{'Date':'5-2020','pos': 106451, 'neu': 601709, 'neg': 75031, 'avg': 0.026123667406806276, 'std': 0.251763838800944, 'Pavg': 0.5055637946096613, 'Pstd': 0.21401404178241293, 'Navg': -0.4446999360262998, 'Nstd': 0.20823238156421955},\
{'Date':'6-2020','pos': 121544, 'neu': 608055, 'neg': 98653, 'avg': 0.017629595461282524, 'std': 0.27530373430917116, 'Pavg': 0.5024601247284276, 'Pstd': 0.21460635106101114, 'Navg': -0.47116231234733913, 'Nstd': 0.22163929558689285},]
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
    
    
    
    