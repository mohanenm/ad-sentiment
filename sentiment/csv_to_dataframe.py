# of course I could have just read these right into a dataframe
# but I want to show multiple steps of the process
# also presently limited in how many times I can ping twitter api under my subscriptions
# could hav

# testing pandas stuff here for the time-being because the issues with model runtime

from nltk.tokenize import word_tokenize
import pickle
import pandas as pd
import training_sentiment as ts

# just doing this to show I have a handle on some basic pandas stuff
tweet_df = pd.read_csv("data_to_model.csv", delimiter=",")
tweet_df.head()
tweet_df.columns = ['date-time', 'tweet']
tweet_df = pd.read_csv("data_to_model.csv", delimiter=",")
tweet_df.head()
tweet_df.columns = ['date-time', 'tweet']
tweet_df = tweet_df.drop('date-time', 1)
tweet_df['tweet'] = tweet_df['tweet'].map(lambda tweet: ts.rmv_noise(word_tokenize(tweet)))

# open our model here for classifying!
classifier_pickle = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_pickle)
#tweet_df['sentiment'] = tweet_df['tweet'].map(lambda tweet: classifier.classify(dict([token, True] for token in tweet)))
tweet_df['sentiment'] = tweet_df['tweet'].map(lambda tweet: classifier.classify(dict([token, True] for token in tweet)))
classifier_pickle.close()










