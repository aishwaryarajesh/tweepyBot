import json
import tweepy

class MyStreamListener(tweepy.StreamListener):
 def __init__(self, api):
    self.api = api
    self.me = api.me()

 def on_status(self, tweet):
    print('{0}:{1}'.format(tweet.user.name,tweet.text))
    
 def on_error(self, status):
    print("Error detected")

#authentication process
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Python", "Django", "Tweepy"], languages=["en"])