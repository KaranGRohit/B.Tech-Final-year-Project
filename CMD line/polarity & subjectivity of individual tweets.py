import tweepy
from textblob import  TextBlob
import json

consumer_key= "ILUh3eXBYqatq60RIoeJ5604C"
consumer_secret= "rsDjyGOXwLU6toyS7KWDBc6tC96BXPCuuXsKiCyEo9YNOPh9P6"

access_token="2201227034-nUyLkNguSvR9LvN6f2KeCKlJivvP9Y60kM9SVgR"
access_token_secret="sv3Qzy42BO0nuTLm1KoaUPEIlSyfqGkptmzPytmTFHjse"

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