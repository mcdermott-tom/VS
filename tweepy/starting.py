import tweepy

consumer_key="YHQotevHcnyRu456NYxBVRSYH"
consumer_secret="ryIoSK3JTswuq3SJH7jbvV3H9qwuVk0uIWjH5M3dJxKbmVVxcS"
access_token="4810976361-ErVSrK9jUdZcduaXXQ6sc4BdZLq1muy9s774mrT"
access_token_secret="mZhTSl6Sb3asgegg7Kjl9QxSnlfxBPuYfOMELsbh7DFyD"
callback = 'oob'

auth = tweepy.OAuthHandler(
    consumer_key, consumer_secret, access_token, access_token_secret, callback
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)