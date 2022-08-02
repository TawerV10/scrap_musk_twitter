import tweepy
import pandas as pd
from config import *

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth, wait_on_rate_limit=True)

cursor = tweepy.Cursor(api.user_timeline, id='elonmusk', tweet_mode='extended', count=200).items()

text = []
likes = []
retweets = []
time = []

for i in cursor:
    text.append(i.full_text)
    likes.append(i.favorite_count)
    retweets.append(i.retweet_count)
    time.append(i.created_at)

df = pd.DataFrame({'time': time, 'text': text, 'likes': likes, 'retweets': retweets})

print(df.shape) # 3200x4
df.to_csv('data.csv', index=False, encoding='utf-8-sig')