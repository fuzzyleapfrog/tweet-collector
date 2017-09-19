#!/usr/bin/python

import ConfigParser
import mysql.connector as mariadb

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
    cursor.execute("SELECT id, tweet_id, people_id, submit FROM tweets ORDER BY submit DESC")
    return cursor


