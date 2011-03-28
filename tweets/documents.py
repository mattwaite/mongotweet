from uuid import uuid4
from mongoengine import *

class Tweet(Document):
    tweet_id = IntField(required=True)
    created_date = DateTimeField(required=True)
    created_day = DateTimeField(required=True)
    created_hour = IntField(required=True)
    text = StringField(required=True)
    screen_name = StringField(required=True)
    profile_photo = StringField(required=True)
    words = ListField(StringField())
