#REST API SAVE MYSQL

import tweepy
import csv
import pandas as pd
import pymysql
import pymysql.cursors

####input your credentials here
consumer_key= 'CHky1yfiABs1YaIGdZfK98Zhg'
consumer_secret= 'tVBpes9lDtvC1F56ov4a4y3msUmeyMYVtVAMZ962UPi93j3uaK'
access_token='966703597625815040-aiC8veIjwoIBxTXG5kPaQHCoED2ZtnF'
access_token_secret='CqJDVqD109b14JTe3gpznBzftWNrhpioZmRLlZUbCbPKY'

conn = pymysql.connect(host='localhost', port=3306, user='root', use_unicode=True, passwd='admin1234', db='tweet',charset='utf8')
cur = conn.cursor()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('textweet.csv', 'a')
csvFile2 = open('fullinfo.csv', 'a')


csvWriter = csv.writer(csvFile)
csvWriter2 = csv.writer(csvFile2)

places = api.geo_search(query="Malaysia", granularity="country")
place_id = places[0].id
count=0
for tweet in tweepy.Cursor(api.search,q=["traffic","traffic jammed","traffic light"],count=10, geocode="3.073281,101.518461,50km",tweet_mode="extended",retweeted=True).items(2000):
	if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
		print ("{}) Created at : {}\nFull text : {}\nLocation : {}\n\n\n".format(count,tweet.created_at, tweet.full_text, tweet.user.location))
		#csvWriter.writerow([tweet.full_text.encode('utf-8'),tweet.user.location])
		#csvWriter2.writerow([tweet])
		cur.execute("INSERT INTO tweetdata (`text`) VALUES (%s)", (tweet))
		count+=1
	conn.commit()
x