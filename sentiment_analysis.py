import re
from textblob import TextBlob
# from textblob.sentiments import NaiveBayesAnalyzer
from deep_translator import GoogleTranslator

def clean_tweet(tweet):
    # text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())
    text_filtred = ' '.join(re.sub("(RT.@\S+|https?://\S+)|(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)",
                            "", tweet).split())
    # print(text)
    re.sub(r"[^a-zA-Z0-9]+", " ", text_filtred)
    return text_filtred

def generate_sentiment_data(tweet):
    analysis = TextBlob(tweet)

    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def convert_text_to_english(text):
    text_translated = GoogleTranslator(source='auto', target='en').translate(text=text)
    return text_translated


# implementar tradução
# Usar google translate
# https://pypi.org/project/googletrans/

# pip install translate
# google-trans-new