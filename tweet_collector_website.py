#!/usr/bin/python

import jinja2
import ConfigParser
import mysql.connector as mariadb
import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import database

def startpage():

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
    user_list = []
    cursor = database.get_latest_users(cursor)
    count = 0
    for id, twitternick, submit in cursor:
        count += 1
        if count > 3:
            break
        dict = {'user': twitternick, 'id': id, 'submit': str(submit)}
        user_list.append(dict)

    # get latest 3 tweets
    tweet_list = []
    cursor = database.get_latest_tweets(cursor)
    count = 0
    for id, tweet_id, twitternick, submit in cursor:
        count += 1
        if count > 3:
            break
        dict = {'id': id, 'tweet_id': tweet_id, 'twitternick': twitternick, 'submit': str(submit)}
        tweet_list.append(dict)

    return template.render(user_list=user_list, tweet_list=tweet_list)

def main():
    print startpage()

if __name__ == "__main__":
    main()


