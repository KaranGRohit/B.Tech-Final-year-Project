from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = 'ILUh3eXBYqatq60RIoeJ5604C'
consumer_secret = 'rsDjyGOXwLU6toyS7KWDBc6tC96BXPCuuXsKiCyEo9YNOPh9P6'

access_token = '2201227034-nUyLkNguSvR9LvN6f2KeCKlJivvP9Y60kM9SVgR'
access_token_secret = 'sv3Qzy42BO0nuTLm1KoaUPEIlSyfqGkptmzPytmTFHjse'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})

app.run(port=5002)