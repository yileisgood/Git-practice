import tweepy
from textblob import TextBlob
import pandas as pd
# Step 1 - Authenticate
consumer_key= 'M3c6G7hUdWK8UO7xons7RO0uS'
consumer_secret= 'JFpenj25MxsdlyokkR9KMUixKQOiHJqJhDRfuZ6guPDIUc1pbO'

access_token='553221310-eMmV4AzmIytu5XDG0cckJqRta3CstUS8g7dFKQ8t'
access_token_secret='7lypFh01slCagqsvHyh08kB4lxZ0T7prdIU5xDrECmPzU'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Brexit')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself

emols = []
for tweet in public_tweets:
    print(tweet.text)
    tweetls = []
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    tweetls.append(tweet.text)
    if analysis.sentiment[1] >= 0.1:
        tweetls.append('positive')
    else:
        tweetls.append('negative')

    emols.append(tweetls)
emodf = pd.DataFrame(emols,columns= ['Text','Polarity label'])
emodf.to_csv('Tweet with Polarity.csv')


