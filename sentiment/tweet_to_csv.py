import csv
import tweepy
from sentiment import api_auth

# open the csv file for training Data, I am going to use this for later
csvFile = open('data_to_model.csv', 'a')
# I am trying to write to the csv file too, initializing a csvWriter does that
csvWriter = csv.writer(csvFile)

# write user input in
# cmp_name = input("company name: ")
# strt_date = input("Start Date(eg., yyyy-mm-dd")
# end_date = input("End Date(eg., yyyy-mm-dd" )

new_search = "nielsen -filter:retweets"

for tweet in tweepy.Cursor(api_auth.api.search,
                           # the check should be
                           q=new_search,
                           # going for simplicity in this case, ideally the consumer entry should be more flexible
                           # interested in last month here, with a more business first model I would be looking at quarters
                           # see comments in csv_dataframe --> query limits under current subscription
                           since="2020-11-20",
                           # using english here, larger scale we would want more accessbility
                           lang="en").items(100):
    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

csvFile.close()
