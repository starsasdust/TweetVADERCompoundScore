In this project, I have developed a python code that could:
1. Flattering the JSON format tweets to python list with each tweet as a dictionary type
   a. Due to the scale of this final project. only text of every tweet is extracted
   b. For extended tweets (longer than 140), the full text is the text for tweets
   c. In this project, the retweeted tweets' text is not included
2. Utilize the VADER[1] classifier from the NLTK to assign polarity classification score to the text of tweet
   a. only compound score[2]
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
To use this code, first call openfiledir() method, which opens every JSON file in the folder path, and extracts the tweets' texts; this method's output is a list of tweet texts.
Then call SentiList() method with the list of tweets text as the parameter; this process would transfer all text into VADER compound scores and outputs a list of scores.
Finally, call monthresult() method, with the list of scores as the parameter, it outputs the python dictionary, which contains various data explained in the 4(c). I didn't continue to put all methods into a for or class because it may cost too much RAM to operate, as explained in 4(b).
In the CSV code, it could transfer all monthly python dictionaries into a CSV file with some added data
a. the percentage of positive/neutral/negative tweets of that month
b. converts date string into date type data

[1]"NLTK :: Natural Language Toolkit", Nltk.org, 2022. [Online]. Available: https://www.nltk.org/. [Accessed: May- 2022].
[2]"Python | Sentiment Analysis using VADER - GeeksforGeeks", GeeksforGeeks, 2021. [Online]. Available: https://www.geeksforgeeks.org/python-sentiment-analysis-using-vader/#:~:text=The%20Compound%20score%20is%20a,1%20(most%20extreme%20positive). [Accessed: 06- Jun- 2022].
