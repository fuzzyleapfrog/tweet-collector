#!/usr/bin/python

def check_url(url):
    import requests
    resp = requests.head(url)
    dict = {}
    if resp.status_code == 404:
        dict['error'] = 1
        return dict
    dict['response'] = resp.status_code
    tweet = url.replace('https://twitter.com/','').replace('http://twitter.com/','').replace('status/','')
    if len(tweet.split('/')) == 2:
        twitternick = tweet.split('/')[0]
        tweet_id = tweet.split('/')[1]
        dict['twitternick'] = twitternick
        dict['tweet_id'] = tweet_id
        dict['error'] = 0
    else:
        dict['error'] = 1
    return dict

