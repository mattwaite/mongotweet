from tweets.documents import Tweet
from operator import itemgetter
from django.shortcuts import render_to_response
from datetime import datetime
import time
from mongoengine import *

def home(request):
    hour_freqs = Tweet.objects.item_frequencies('created_hour', normalize=False)
    top_hours = sorted(hour_freqs.items(), key=itemgetter(0), reverse=False)[:24]
    tophours = []
    for object in top_hours:
        tophours.append((int(object[0]), object[1]))
    tophours.sort()
    day_freqs = Tweet.objects.order_by('+created_day').item_frequencies('created_day', normalize=False)
    top_days = sorted(day_freqs.items(), key=itemgetter(0), reverse=False)
    screen_freqs = Tweet.objects.item_frequencies('screen_name', normalize=False)
    top_screens = sorted(screen_freqs.items(), key=itemgetter(1), reverse=True)[:20]
    word_freqs = Tweet.objects.item_frequencies('words', normalize=False)
    top_words = sorted(word_freqs.items(), key=itemgetter(1), reverse=True)[1:21]
    return render_to_response('homepage.html', {
        'tophours': tophours,
        'top_days': top_days,
        'top_screens': top_screens,
        'top_words': top_words,
    })