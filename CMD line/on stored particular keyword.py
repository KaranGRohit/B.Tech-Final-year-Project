import json
import requests
import re
from requests_oauthlib import OAuth1
from textblob import TextBlob
from collections import Counter


api_key = ''
api_secret_key = ''
auth = OAuth1(api_key, api_secret_key)
screen_name = 'realDonaldTrump'
url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+screen_name+"&count=200"
ans = requests.get(url, auth=auth)
jtweet = json.loads(ans.text)

twi_li=[]
for x in range(1,200):
	#print (x)
	a=jtweet[x]['text']
	clean_var= ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", a).split())
	a1=TextBlob(clean_var)
	if (a1.sentiment.polarity > 0):
		twi_li.append("positive")
	elif (a1.sentiment.polarity < 0):
		twi_li.append("negative")
	else:
		twi_li.append("neutral")
twi_li_count=Counter(twi_li)
b=[]
for x in twi_li_count:
	b.append(twi_li_count[x])
key_max=max(b)
max_words = [key for key,value in twi_li_count.items() if value==key_max]
print("The overall sentiment analysis: "+ str(*max_words)) # "*" is used to remove brackets



