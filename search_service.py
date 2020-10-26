import tweepy
from config import credentials

def search_tweet(name_query):
    auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
    auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])

    api = tweepy.API(auth)
    tweets = api.search(q=name_query, tweet_mode='extended', count=90)
    return tweets
