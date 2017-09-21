#!/usr/bin/python

import jinja2
import ConfigParser
import mysql.connector as mariadb
import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import database

def startpage(url):

    CONFIGFILE = '/etc/tweet-collector.cfg'

    # get config
    config = ConfigParser.ConfigParser()
    config.readfp(open(CONFIGFILE))

    # connect to database
    mariadb_connection = mariadb.connect(user=config.get('Database','USER'),
                                         password=config.get('Database','PW'),
                                         database=config.get('Database','NAME'))
    cursor = mariadb_connection.cursor()

    # get template
    currentpath = os.path.dirname(__file__)
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(currentpath),
    )
    template = env.get_template('tweet_collector_website.html')

    # get latest 3 users
    user = []
    cursor = database.get_latest_users(cursor)
    count = 0
    for id, twitternick, submit in cursor:
        link = 'https://twitter.com/'+twitternick
        count += 1
        if count > 3:
            break
        dict = {'user': twitternick,
                'id': id,
                'submit': str(submit),
                'link': link}
        user.append(dict)

    # get latest 3 tweets
    tweet = []
    cursor = database.get_latest_tweets(cursor)
    count = 0
    for id, tweet_id, twitternick, submit in cursor:
        link = 'https://twitter.com/'+twitternick+'/status/'+tweet_id
        profile = 'https://twitter.com/'+twitternick
        count += 1
        if count > 3:
            break
        dict = {'id': id,
                'tweet_id': tweet_id,
                'twitternick': twitternick,
                'profile': profile,
                'submit': str(submit),
                'link': link}
        tweet.append(dict)

    collect = []
    if url != "":
        dict = {'url': url,
                'text': 'The following tweet has been collected: '}
        collect.append(dict)

    return template.render(user=user, tweet=tweet, collect=collect)

def main():
    print startpage()

if __name__ == "__main__":
    main()


