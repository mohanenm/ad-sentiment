# of course I could have just read these right into a dataframe
# but I want to show multiple steps of the process
# also presently limited in how many times I can ping twitter api under my subscriptions
# could hav
import pandas as pd

# import tweet_to_csv

tweet_data = pd.read_csv("data_to_model.csv", delimiter=",")
tweet_data.head()
tweet_data.columns = ['date-time', 'tweet']

