import tweepy
from textblob import TextBlob

#import twitter APIS/credentials
consumer_key = "CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET"

#authentication process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
    
#create api
api = tweepy.API(auth)

#create a tweet
api.update_status("Hello Tweepy")

#load tweets
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    print("")

#get user object for twitter
user = api.get_user('tesla')
print("User details:")
print(user.screen_name)
print(user.description)
print(user.followers_count)
print(user.location)
print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)

#following accounts
print("Tesla is a really amazing company, let me follow another tech account, and like some cool posts!")
api.create_friendship("google")

#like posts
tweets = api.home_timeline(count=3)
tweet = tweets[0]
print("Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)

#combine libraries
myTweets = ""
public_tweets = api.home_timeline()
for tweet in public_tweets:
    myTweets += tweet.text
    myTweets += ""
blob = TextBlob(myTweets)