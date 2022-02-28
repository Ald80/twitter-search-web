from config import authentication
from sentiment_analysis import generate_sentiment_data, clean_tweet, convert_text_to_english

from threading import Thread


def search_tweet(name_query):
    api = authentication()
    tweets = api.search(q=name_query, tweet_mode='extended', count=100)

    tweets_object = create_object_tweets(tweets)
    # print(tweets_object)
    return tweets_object
    # instalar o text blob e fazer o restante ...

def create_object_tweets(tweets):
    tweets_object = []

    for tweet in tweets:

        parsed_tweet = {}

        text_cleaned = clean_tweet(tweet.full_text)
        text_translated = convert_text_to_english(text_cleaned)
        parsed_tweet['full_text'] = tweet.full_text
        parsed_tweet['full_text_cleaned'] = text_cleaned
        parsed_tweet['sentiment'] = generate_sentiment_data(text_translated)
        print(parsed_tweet['full_text'])
        print(parsed_tweet['sentiment'])
        if tweet.retweet_count > 0:
            if parsed_tweet not in tweets_object:
                tweets_object.append(parsed_tweet)
        else:
            tweets_object.append(parsed_tweet)

    return tweets_object

# https://deep-translator.readthedocs.io/en/latest/modules.html#translators


# implement front end, displaying datas in one graphic
# calculate porcent positive, negative and neutral and displaying in graphic
# implement unit test in project
# implement thred or parallel execution to execute convert_text_to_english function in parallel
