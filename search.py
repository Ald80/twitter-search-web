from config import authentication

def search_tweet(name_query):

    api = authentication()
    tweets = api.search(q=name_query, tweet_mode='extended', count=90)
    return tweets


