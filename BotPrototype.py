import botometer
import tweepy
import pandas as pd
import numpy as np
from textblob import TextBlob
from tweepy import StreamListener
from tweepy import API
from tweepy import Stream
from tweepy import Cursor
from tweepy import OAuthHandler
import twitterkeys
import requests


auth = tweepy.OAuthHandler('0mB58XYsHV0UYwICTIgFMA4O7', 'hxyU4w4CLhkfL37RqxO1kL1x7aYN0QPAxK9f5YkQ0EUbbBUUqi')
auth.set_access_token('1375903355835322370-lplVtCJ9wAySl84Sw5A2PaFiKe6Q5e', 'JwVjt41o6onLHPgDNsZuXn2HYf47COeMvDZZYbQ30orpx')
api = tweepy.API(auth)
rapidapi_key = "81b4263176msh310026d8be8938dp14cf4cjsnc44472933c61"
twitter_app_auth = {
    'consumer_key': '0mB58XYsHV0UYwICTIgFMA4O7',
    'consumer_secret': 'hxyU4w4CLhkfL37RqxO1kL1x7aYN0QPAxK9f5YkQ0EUbbBUUqi',
    'access_token': '1375903355835322370-lplVtCJ9wAySl84Sw5A2PaFiKe6Q5e',
    'access_token_secret': 'JwVjt41o6onLHPgDNsZuXn2HYf47COeMvDZZYbQ30orpx',
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a sequence of accounts
accounts = api.get_user('twitter')
for screen_name, result in bom.check_accounts_in(accounts):
    # Do stuff with `screen_name` and `result`
    print (screen_name,result)



