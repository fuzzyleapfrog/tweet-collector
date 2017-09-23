#!/usr/bin/python

def check_url(url):
    dict = {}
    tweet = url.replace('https://twitter.com/','').replace('http://twitter.com/','').replace('status/','')
    if len(tweet.split('/')) == 2:
        twitternick = tweet.split('/')[0]
        tweet_id = tweet.split('/')[1]
        dict = {'twitternick': twitternick,
                'tweet_id': tweet_id}
    return dict

