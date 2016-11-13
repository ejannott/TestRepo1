# Ethan Jannott
# ejannott
# 22235024

# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

# My Twitter access codes
access_token = "62430622-CPwPMVGNBqTXwFEY136dYrbmPvGG0nwmS7adaNTBo"
access_token_secret = "BofxfCapRiDS3vw481Dwa3GLyU9mc9MhDOVsiRBvDL3Mj"
consumer_key = "po6eW08LkTk0YWeYW50iWFsvT"
consumer_secret = "6M781e2jTyXGWADOw8aAEVWKlC3Licbu7uSOrquUGz49QB5EWB"

# # # Lines 18-23 taken from pythoncentral.io
# Boilerplate code here
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

public_tweets = api.search('umsi')

totalTweetCount = 0
subjectivity = 0.0
polarity = 0.0

for tweet in public_tweets:
	totalTweetCount += 1
	print(tweet.text + "\n")
	analysis = TextBlob(tweet.text)
	subjectivity = analysis.subjectivity
	polarity = analysis.polarity

print("Average subjectivity is ", subjectivity/totalTweetCount)
print("Average polarity is ", polarity/totalTweetCount)