from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

def percentage(part, whole):
    return 100*float(part)/float(whole)

consumerKey = "ILUh3eXBYqatq60RIoeJ5604C"
consumerSecret = "rsDjyGOXwLU6toyS7KWDBc6tC96BXPCuuXsKiCyEo9YNOPh9P6"
accessToken = "2201227034-nUyLkNguSvR9LvN6f2KeCKlJivvP9Y60kM9SVgR"
accessTokenSecret = "sv3Qzy42BO0nuTLm1KoaUPEIlSyfqGkptmzPytmTFHjse"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

searchTerm = input("Enter keyword\hashtag to search about: ")

noOfSearchTerms = int(input("Enter How many tweets to analyze: "))

tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if(analysis.sentiment.polarity == 0):
        neutral += 1

    elif(analysis.sentiment.polarity < 0):
        negative += 1

    elif(analysis.sentiment.polarity > 0):
        positive += 1


positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)
polarity = percentage(polarity, noOfSearchTerms)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')


print("How people are reacting on "+ searchTerm + " by analyzing "+ str(noOfSearchTerms) + " Tweets. ")

if(polarity == 0):
    print("Nuetral")

elif(polarity > 0.00):
    print("Positive")

elif(polarity < 0.00):
    print("Negative")



labels = ['Positive  ['+str(positive)+' %]','Neutral  ['+str(neutral)+' %]','Negative  ['+str(negative)+' %]']

sizes = [positive, neutral, negative]

colors = ['yellowgreen', 'gold', 'red']

patches, text = plt.pie(sizes, colors=colors, startangle=90)

plt.legend(patches, labels, loc="best")

plt.title('How people are reacting on '+ searchTerm + ' by analyzing '+ str(noOfSearchTerms) + ' Tweets. ')

plt.axis('equal')

plt.tight_layout()

plt.show()
