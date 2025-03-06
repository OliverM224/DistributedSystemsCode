import json
import tweepy
#importing libraries

def lambda_handler(event, context):
    

    sensorJSON = json.dumps(event)#converting sensor data into dictionary format.
    sensorData = json.loads(sensorJSON)#converting inputted data from dictionary to string format accessible to python

    DateTime = sensorData['dateTime']
    Location = sensorData['Location']
    Severity = sensorData['Severity']

    client = tweepy.Client(
                consumer_key = ('API_KEY'),
                consumer_secret=('SECRET_API_KEY'),
                access_token=('ACCESS_TOKEN'),
                access_token_secret=('SECRET_ACCESS_TOKEN')
        ) 
    tweet_text = "Attention! There is a {} risk flooding alert close to the {}. \nTime of incident: {}".format(Severity, Location, DateTime) +""

    response = client.create_tweet(text=tweet_text)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Program executed.')
    }
