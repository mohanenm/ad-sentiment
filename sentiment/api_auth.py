import tweepy
from tweepy import OAuthHandler

###consumer keys here, but not putting those on git


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
