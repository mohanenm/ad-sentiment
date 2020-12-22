import tweepy
from tweepy import OAuthHandler

#consumer keys here, but not putting those on git
consumer_key = "Mu9jiPsTDG3WTUqrjZC62NsLk"
consumer_secret = "Gmvcj0uQ5Ubo0CQhCwj5fzr7bqbJQQfQv0ACdGphsPTblbYctX"
access_token = "863265431691436032-Jf49bb4gU9Ln2hTO2H37nUqZmEt3uZ1"
access_secret = "5OUsQsUVikYmGbTAqS2nlczxg9rwUHmkMt65vmYtxwUQL"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
