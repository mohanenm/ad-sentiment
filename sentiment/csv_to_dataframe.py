# of course I could have just read these right into a dataframe
# but I want to show multiple steps of the process
# also presently limited in how many times I can ping twitter api under my subscriptions
# could hav

from nltk.tokenize import word_tokenize
# import tweet_to_csv
import pandas as pd
import training_sentiment as ts


# just doing this to show I have a handle on some basic pandas stuff
tweet_df = pd.read_csv("data_to_model.csv", delimiter=",")
tweet_df.head()
tweet_df.columns = ['date-time', 'tweet']
tweet_df = tweet_df.drop('date-time', 1)

