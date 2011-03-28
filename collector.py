from django.core.management import setup_environ
from django.template.defaultfilters import striptags

import sys
sys.path.append('/path/to/your/django/projects/')
from twitterfact import settings
setup_environ(settings)

from mongotweet.tweets.documents import Tweet
import twitter, time, string
from datetime import datetime

api = twitter.Api()

term = "YOURTERMHERE"

p = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

nonwords = ["the", "The", "and", "And", "an", "An", "if", "If", "of", "Of", "that", "That", "A", "a", "On", "on", "Or", "or", "Is", "is", "This", "this", "it", "It", "You", "you", "Its", "its", "It's", "it's", "For", "for", "to", "To", "|", "Than", "than"]

for i in p: 
    tweets = api.GetSearch(term, per_page=100, page=i)
    for object in tweets:
        tid = object.id
        t = Tweet.objects(tweet_id=tid)
        if t:
            continue
        else:
            tweet_date = object.created_at
            tweet_date = time.strptime(tweet_date, "%a, %d %b %Y %H:%M:%S +0000")
            tweet_hour = tweet_date.tm_hour
            tweet_day = datetime(tweet_date.tm_year, tweet_date.tm_mon, tweet_date.tm_mday)
            tweet_date = datetime(tweet_date.tm_year, tweet_date.tm_mon, tweet_date.tm_mday, tweet_date.tm_hour, tweet_date.tm_min, tweet_date.tm_sec)
            tweet_words = object.text.split(' ')
            tweet_words = list(set(tweet_words) - set(nonwords))
            ent = Tweet(tweet_id=object.id, created_date=tweet_date, created_hour=tweet_hour, created_day=tweet_day, text=object.text, screen_name=object.user.screen_name, profile_photo=object.user.profile_image_url, words=tweet_words).save()
    time.sleep(3)