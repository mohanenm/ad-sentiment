import csv
import tweepy
import api_auth

# open the csv file for training Data, I am going to use this for later
csvFile = open('sentiment_training.csv', 'a')
# I am trying to write to the csv file too, initializing a csvWriter does that
csvWriter = csv.writer(csvFile)

# write user input in
cmp_name = input("company name: ")
strt_date = input("Start Date(eg., yyyy-mm-dd")
end_date = input("End Date(eg., yyyy-mm-dd" )

for tweet in tweepy.Cursor(api_auth.api.search,
                           # the check should be
                           q = cmp_name,
                           # going for simplicity in this case, ideally the consumer entry should be more flexible
                           since = strt_date,
                           until = end_date,
                           # using english here, larger scale we would want more accessbility
                           lang = "en").items():

    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

csvFile.close()
