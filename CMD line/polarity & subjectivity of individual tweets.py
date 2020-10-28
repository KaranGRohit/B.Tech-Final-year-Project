import tweepy
from textblob import  TextBlob
import json

consumer_key= ""
consumer_secret= ""

access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class StdOutListener(tweepy.StreamListener):
    counter = 0

    def on_data(self, data):
        tweet = json.loads(data)
        analysis = TextBlob(tweet['text'])
        print(tweet['text'])
        print(analysis.sentiment)
        print('-------------------------------------------------------------')
        return True

    def on_error(self, status):
        print(status)

    def on_status(self, status):
        global counter
        counter = counter + 1
        if counter < 5:
            return True
        else:
            return False

myStream = tweepy.Stream(auth = api.auth, listener = StdOutListener())
myStream.filter(track = ["Trump"], languages=["en"])


public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print('-------------------------------------------------------------')
