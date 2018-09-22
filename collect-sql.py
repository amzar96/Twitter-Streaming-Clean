#SAVE IN MYSQL STREAMING API

import pymysql
import tweepy
import time
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import pymysql.cursors


ckey= 'CHky1yfiABs1YaIGdZfK98Zhg'
csecret= 'tVBpes9lDtvC1F56ov4a4y3msUmeyMYVtVAMZ962UPi93j3uaK'
atoken= '966703597625815040-aiC8veIjwoIBxTXG5kPaQHCoED2ZtnF'
asecret= 'CqJDVqD109b14JTe3gpznBzftWNrhpioZmRLlZUbCbPKY'



conn = pymysql.connect(host='localhost', port=3306, user='root', use_unicode=True, passwd='admin1234', db='twitter',charset='utf8')
cur = conn.cursor()

if conn.open:
    pass

class listener(StreamListener):

 def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        a=0
        #username = all_data["user"]["screen_name"]
        print(tweet)
        cur.execute("INSERT INTO tweetdata (`text`) VALUES (%s)", (tweet))
        conn.commit()
        #print (tweet)
        return True

def on_error(self, status):
    print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(locations=[101.418145,2.756636,101.736528,3.277724])

cur.close()
conn.close()