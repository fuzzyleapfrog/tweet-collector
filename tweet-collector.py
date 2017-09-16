#!/usr/bin/python

import ConfigParser
import mysql.connector as mariadb

def print_user(cursor):
    for id, twitternick in cursor:
        print("ID: {}, Twitternick: {}").format(id,twitternick)    

def get_user(cursor,key,value):
    query = "SELECT id, twitternick FROM people WHERE {} = '{}'".format(key,value)
    cursor.execute(query)
    print_user(cursor)
    return cursor

def get_all_users(cursor):
    cursor.execute("SELECT id, twitternick FROM people")
    print_user(cursor)
    return cursor

def insert_user(cursor,twitternick):
    query = "INSERT INTO people (id, twitternick) VALUES (NULL, '{}')".format(twitternick)
    cursor.execute(query)
    print_user(cursor)
    return cursor

def delete_user(cursor,key,value):
    query = "DELETE FROM people WHERE {} = '{}'".format(key,value)
    cursor.execute(query)
    print_user(cursor)
    return cursor

def print_tweet(cursor):
    for id, tweet_id, people_id in cursor:
        print("ID: {}, Tweet-ID: {}, User-ID: {}").format(id,tweet_id,people_id)    

def get_tweet(cursor,key,value):
    query = "SELECT id, tweet_id, people_id FROM tweets WHERE {} = '{}'".format(key,value)
    cursor.execute(query)
    print_tweet(cursor)
    return cursor
    
def get_all_tweets(cursor):
    cursor.execute("SELECT id, tweet_id, people_id FROM tweets")
    print_tweet(cursor)
    return cursor

def insert_tweet(cursor,tweet_id,people_id):
    query = "INSERT INTO tweets (id, tweet_id, people_id) VALUES (NULL, '{}', {})".format(tweet_id,people_id)
    cursor.execute(query)
    print_user(cursor)
    return cursor

def delete_tweets(cursor,key,value):
    query = "DELETE FROM tweets WHERE {} = '{}'".format(key,value)
    cursor.execute(query)
    print_user(cursor)
    return cursor

def main():

    # get config
    config = ConfigParser.ConfigParser()
    config.readfp(open('config.cfg'))

    # connect to database
    mariadb_connection = mariadb.connect(user=config.get('Database','USER'),
                                         password=config.get('Database','PW'),
                                         database=config.get('Database','NAME'))
    cursor = mariadb_connection.cursor()

    # ---- PEOPLE ----
    
    # define already existing users
    twitternick = 'HeptaSean'
    id = 4

    # get one user by twitternick
    print 'get one user by twitternick'
    cursor = get_user(cursor,'twitternick',twitternick)
    # get one user by id
    print 'get one user by id'
    cursor = get_user(cursor,'id',id)

    # get all users
    print 'get all users'
    cursor = get_all_users(cursor)

    # define test user
    twitternick = 'testnick'

    # insert user into table people
    print 'insert user with twitternick %s in table people' % twitternick
    insert_user(cursor,twitternick)

    # get all users
    print 'get all users'
    cursor = get_all_users(cursor)

    # delete user from table people
    print 'delete user %s' % twitternick
    delete_user(cursor,'twitternick',twitternick)

    # get all users
    print 'get all users'
    cursor = get_all_users(cursor)

    # --- TWEETS ---

    # define already existing tweet
    tweet_id = '877880899764977664'
    id = 1
    people_id = 1

    # get one tweet by tweet id
    print 'get one tweet by tweet id'
    cursor = get_tweet(cursor,'tweet_id',tweet_id)
    # get one tweet by id
    print 'get one tweet by id'
    cursor = get_tweet(cursor,'id',id)
    # get tweets by user id
    print 'get one tweet by user id'
    cursor = get_tweet(cursor,'people_id',people_id)

    # get all tweets
    print 'get all tweets'
    cursor = get_all_tweets(cursor)

    # define test tweet
    tweet_id = '908758168733405184'
    people_id = 4

    # insert tweet into table tweets
    print 'insert tweet %s of user with id %d in table tweets' % (tweet_id, people_id)
    insert_tweet(cursor,tweet_id,people_id)

    # get all tweets
    print 'get all tweets'
    cursor = get_all_tweets(cursor)

    # delete tweet from table tweets by tweet id
    print 'delete tweet by tweet id %s' % tweet_id
    delete_tweets(cursor,'tweet_id',tweet_id)

    # get all tweets
    print 'get all tweets'
    cursor = get_all_tweets(cursor)

    # define test tweet
    tweet_id = '908758168733405184'
    people_id = 4

    # insert tweet into table tweets
    print 'insert tweet %s of user with id %d in table tweets' % (tweet_id, people_id)
    insert_tweet(cursor,tweet_id,people_id)

    # define test tweet
    tweet_id = '908392946051026945'
    people_id = 4

    # insert tweet into table tweets
    print 'insert tweet %s of user with id %d in table tweets' % (tweet_id, people_id)
    insert_tweet(cursor,tweet_id,people_id)

    # get all tweets
    print 'get all tweets'
    cursor = get_all_tweets(cursor)

    # delete tweet from table tweets by people id
    print 'delete tweets by user id %s' % people_id
    delete_tweets(cursor,'people_id',people_id)

    # get all tweets
    print 'get all tweets'
    cursor = get_all_tweets(cursor)

if __name__ == "__main__":
    main()


