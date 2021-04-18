import tweepy

auth = tweepy.OAuthHandler("5Mu69JuW60hOnfccz1gq9ZZoK", "CAlSbfaV1paRLeisoCmN8DheKyl4wOd4tAdOgJt4pcGCjSkxhH")
auth.set_access_token("1375903355835322370-1VOGj6Od1dfHcBwIqRiyDdGycnCLTw", "D8A0ZlfWJUIsoTf3yw1yvwtbhoiujGdydDwY2zw2YUzsP")

api = tweepy.API(auth)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
   

