import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'H6z8EvUvLuH0Wh1u5mrHHvixp'
consumer_secret = 'Ur5t9drG9WXwHPfNoTVn9bKSwOODbWBCVHQeRYCSHJJFnsAUee'
access_token = '1179862702958809098-eIR9HIviXeOzYpVI3SuJjfmlO4jEjj'
access_token_secret = 'i50yVujxc64CXZsPalKeDbjqUr3BEwsxGyBAsb2BlzSV8'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#DLCIA",count=100,                          
                           since="2017-04-03").items():
    print (tweet.entities['media'][0]['media_url'])
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.entities['media'][0]['media_url']])


