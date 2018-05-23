import textblob as textblob
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob
import pymysql.cursors

# consumer key, consumer secret, access token, access secret.
consumer_key= 
consumer_secret= 
access_token=
access_token_secret=

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin1234', db='tweet')
cur = conn.cursor()

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


class StdOutlistener(StreamListener):
    def on_data(self, status):
        all_data = json.loads(status)
        #tweet = TextBlob(all_data["text"])

        #Add the 'sentiment data to all_data
        #all_data['sentiment'] = tweet.sentiment
        #if any(c in all_data['text'] for c in (["traffic slow","traffic suck","jammed","traffic jammed","traffic"])):
            #print(("\nFOUND!!\n {}").format(all_data['text']))
            
        print(all_data['text'])
        # Open json text file to save the tweets
        with open('data/tweetla.json', 'a') as tf:
                # Write a new line
            tf.write('\n\n')

                # Write the json data directly to the file
            json.dump(all_data, tf)

            #tf.write(all_data)

        return True

    def on_error(self, status):
        print(status)
        return True


twitterStream = Stream(auth, StdOutlistener())
twitterStream.filter(locations=[101.418145,2.756636,101.736528,3.277724])