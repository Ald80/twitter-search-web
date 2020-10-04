import tweepy

consumer_key = 'WQmvg3QzIXcLNyDHjWVyzVanP'
consumer_secret = 'YelNa3r75LiWEow6Jyq1tl8XCqHLOzAjvtcqnzGBmzvdOWoM7u'

access_token = '1089501322854969344-X4KTnn9kY4UqAhuIrjmtg1m5uBKPyy'
access_token_secret = '1oHd4twnym9KG2bkH2c3tD5G7cOrN1yHrGoprhaWCuwBV'

def search_tweet(name_query):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    tweets = api.search(q=name_query, tweet_mode='extended', count=90)
    return tweets
