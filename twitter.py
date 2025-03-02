import tweepy
import os

def post_tweet():

        client = tweepy.Client(
                consumer_key=os.getenv("API_KEY"),
                consumer_secret=os.getenv("SECRET_API_KEY"),
                access_token=os.getenv("ACCESS_TOKEN"),
                access_token_secret=os.getenv("SECRET_ACCESS_TOKEN")
        ) 
        tweet_text = "WARNING: The Ipswich Waterfront has been flooded. Residents are advised to avoid the area. Star Lane has been closed."

        response = client.create_tweet(text=tweet_text)

        return{
                "statusCode": 200
        }

        print(response)

post_tweet()