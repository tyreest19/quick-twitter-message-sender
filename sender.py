from tweepy import *
import tweepy
class Sender():
    api = ""
    def __init__(self,consumer_key,consumer_secret,access_token,access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def sendMessage(self,screenName,text1):
        self.api.send_direct_message(screen_name=screenName,text=text1)














































