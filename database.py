#!/usr/bin/python

import ConfigParser
import mysql.connector as mariadb

def connect_to_db():
    CONFIGFILE = '/etc/tweet-collector.cfg'
    # get config
    config = ConfigParser.ConfigParser()
    config.readfp(open(CONFIGFILE))
    # connect to database
    mariadb_connection = mariadb.connect(user=config.get('Database','USER'),
                                         password=config.get('Database','PW'),
                                         database=config.get('Database','NAME'))
    cursor = mariadb_connection.cursor()
    return cursor

def print_user(cursor):
    string = ''
    for id, twitternick, submit in cursor:
        string += "ID: {}, Twitternick: {}".format(id,twitternick)+'\n'
    return string

def get_user(cursor,key,value):
    query = "SELECT id, twitternick, submit FROM people WHERE {} = '{}'".format(key,value)
    cursor.execute(query)
    return cursor

def get_all_users(cursor):
    cursor.execute("SELECT id, twitternick, submit FROM people")
    return cursor

def insert_user(cursor,twitternick):
    query = "INSERT INTO people (id, twitternick) VALUES (NULL, '{}')".format(twitternick)
    cursor.execute(query)
    return cursor

def delete_user(cursor,key,value):
    query = "DELETE FROM people WHERE {} = '{}'".format(key,value)
    cursor.execute(query)
    return cursor

def get_latest_users(cursor):
    cursor.execute("SELECT id, twitternick, submit FROM people ORDER BY submit DESC")
    return cursor

def print_tweet(cursor):
    string = ''
    for id, tweet_id, people_id, submit in cursor:
        string += "ID: {}, Tweet-ID: {}, User-ID: {}".format(id,tweet_id,people_id)+'\n'
    return string

def print_latest_tweets(cursor):
    string = ''
    for id, tweet_id, twitternick, submit in cursor:
        string += "ID: {}, Tweet-ID: {}, Twitternick: {}".format(id,tweet_id,twitternick)+'\n'
    return string

def get_tweet(cursor,key,value):
    query = "SELECT id, tweet_id, people_id, submit FROM tweets WHERE {} = '{}'".format(key,value)
    cursor.execute(query)
    return cursor
    
def get_all_tweets(cursor):
    cursor.execute("SELECT id, tweet_id, people_id, submit FROM tweets")
    return cursor

def insert_tweet(cursor,tweet_id,people_id):
    query = "INSERT INTO tweets (id, tweet_id, people_id) VALUES (NULL, '{}', {})".format(tweet_id,people_id)
    cursor.execute(query)
    return cursor

def delete_tweets(cursor,key,value):
    query = "DELETE FROM tweets WHERE {} = '{}'".format(key,value)
    cursor.execute(query)
    return cursor

def get_latest_tweets(cursor):
    cursor.execute("SELECT tweets.id, tweets.tweet_id, people.twitternick, tweets.submit FROM tweets INNER JOIN people ON tweets.people_id = people.id ORDER BY tweets.submit DESC")
    return cursor

def check_tweet_for_people(url):
    tweet = url.replace('https://twitter.com/','').replace('http://twitter.com/','').replace('status/','')
    twitternick = tweet.split('/')[0]
    tweet_id = tweet.split('/')[1]
    string = url+', '+twitternick+', '+tweet_id+'\n'
#    query = "SELECT id, twitternick, submit FROM people WHERE {} = '{}'".format('twitternick',twitternick)
#    cursor.execute(query)
#    return cursor
    return string
