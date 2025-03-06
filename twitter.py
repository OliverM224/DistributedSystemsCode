import json
import tweepy
#importing libraries

def lambda_handler(event, context):
    # TODO implement

    sensorJSON = json.dumps(event)#converting sensor data into dictionary format.
    sensorData = json.loads(sensorJSON)#converting inputted data from dictionary to string format accessible to python

    DateTime = sensorData['dateTime']
    Location = sensorData['Location']
    Severity = sensorData['Severity']

    client = tweepy.Client(
                consumer_key = ('4vXXR6mVX0FHY15qWqkRCFth2'),
                consumer_secret=('5C70WZaj1xpnE0r9kZpGJBjiFPK1E28txIx6mi8eDZC4eJ7XYd'),
                access_token=('1895139284509691904-j95JzD2lLIDypBk5jXmumwB7mnjLpX'),
                access_token_secret=('Y1ZFR8FiaO2prStZSwzaaqabWNJ22xB3XLL6kg8APjADZ')
        ) 
    tweet_text = "Attention! There is a {} risk flooding alert close to the {}. \nTime of incident: {}".format(Severity, Location, DateTime) +""

    response = client.create_tweet(text=tweet_text)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Program executed.')
    }
