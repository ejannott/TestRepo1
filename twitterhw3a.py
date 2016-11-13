# Ethan Jannott
# ejannott
# 22235024

# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy

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

image = "lamborghini.jpg"
try:
	api.update_with_media(image, status="Test tweet for UMSI - dope ride. #UMSI206 #Proj3")
	print("- Tweet sucessfully posted -")
except:
	print ("- Tweet failed to post -")