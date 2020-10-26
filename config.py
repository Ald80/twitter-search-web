from dotenv import load_dotenv
import os

load_dotenv()

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")

access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

credentials = {
    "consumer_key": consumer_key,
    "consumer_secret": consumer_secret,
    "access_token": access_token,
    "access_token_secret": access_token_secret
}

