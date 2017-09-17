#!/usr/bin/python

import ConfigParser
import mysql.connector as mariadb

def print_user(cursor):
    string = ''
    for id, twitternick in cursor:
        string += "ID: {}, Twitternick: {}".format(id,twitternick)+'\n'
    return string

def get_user(cursor,key,value):
    query = "SELECT id, twitternick FROM people WHERE {} = '{}'".format(key,value)
    cursor.execute(query)
    return cursor

def get_all_users(cursor):
    cursor.execute("SELECT id, twitternick FROM people")
    return cursor

def insert_user(cursor,twitternick):
    query = "INSERT INTO people (id, twitternick) VALUES (NULL, '{}')".format(twitternick)
    cursor.execute(query)
    return cursor

def delete_user(cursor,key,value):
    query = "DELETE FROM people WHERE {} = '{}'".format(key,value)
    cursor.execute(query)
    return cursor

def print_tweet(cursor):
    string = ''
    for id, tweet_id, people_id in cursor:
        string += "ID: {}, Tweet-ID: {}, User-ID: {}".format(id,tweet_id,people_id)+'\n'
    return string

def get_tweet(cursor,key,value):
    query = "SELECT id, tweet_id, people_id FROM tweets WHERE {} = '{}'".format(key,value)
    cursor.execute(query)
    return cursor
    
def get_all_tweets(cursor):
    cursor.execute("SELECT id, tweet_id, people_id FROM tweets")
    return cursor

def insert_tweet(cursor,tweet_id,people_id):
    query = "INSERT INTO tweets (id, tweet_id, people_id) VALUES (NULL, '{}', {})".format(tweet_id,people_id)
    cursor.execute(query)
    return cursor

def delete_tweets(cursor,key,value):
    query = "DELETE FROM tweets WHERE {} = '{}'".format(key,value)
    cursor.execute(query)
    return cursor

def test_mode():

    CONFIG = '/etc/tweet-collector.cfg'

    # get config
    config = ConfigParser.ConfigParser()
    config.readfp(open(CONFIG))

    # connect to database
    mariadb_connection = mariadb.connect(user=config.get('Database','USER'),
                                         password=config.get('Database','PW'),
                                         database=config.get('Database','NAME'))
    cursor = mariadb_connection.cursor()

    string = ''

    # ---- PEOPLE ----
    
    # define already existing users
    twitternick = 'HeptaSean'
    id = 4

    # get one user by twitternick
    string += 'get one user by twitternick'+'\n'
    cursor = get_user(cursor,'twitternick',twitternick)
    string += print_user(cursor)
    # get one user by id
    string += 'get one user by id'+'\n'
    cursor = get_user(cursor,'id',id)
    string += print_user(cursor)

    # get all users
    string += 'get all users'+'\n'
    cursor = get_all_users(cursor)
    string += print_user(cursor)

    # define test user
    twitternick = 'testnick'

    # insert user into table people
    string += 'insert user with twitternick %s in table people\n' % twitternick
    insert_user(cursor,twitternick)

    # get all users
    string += 'get all users'+'\n'
    cursor = get_all_users(cursor)
    string += print_user(cursor)

    # delete user from table people
    string += 'delete user %s\n' % twitternick
    delete_user(cursor,'twitternick',twitternick)

    # get all users
    string += 'get all users'+'\n'
    cursor = get_all_users(cursor)
    string += print_user(cursor)

    # --- TWEETS ---

    # define already existing tweet
    tweet_id = '877880899764977664'
    id = 1
    people_id = 1

    # get one tweet by tweet id
    string += 'get one tweet by tweet id'+'\n'
    cursor = get_tweet(cursor,'tweet_id',tweet_id)
    string += print_tweet(cursor)
    # get one tweet by id
    string += 'get one tweet by id'+'\n'
    cursor = get_tweet(cursor,'id',id)
    string += print_tweet(cursor)
    # get tweets by user id
    string += 'get one tweet by user id'+'\n'
    cursor = get_tweet(cursor,'people_id',people_id)
    string += print_tweet(cursor)

    # get all tweets
    string += 'get all tweets'+'\n'
    cursor = get_all_tweets(cursor)
    string += print_tweet(cursor)

    # define test tweet
    tweet_id = '908758168733405184'
    people_id = 4

    # insert tweet into table tweets
    string += 'insert tweet %s of user with id %d in table tweets\n' % (tweet_id, people_id)
    insert_tweet(cursor,tweet_id,people_id)

    # get all tweets
    string += 'get all tweets'+'\n'
    cursor = get_all_tweets(cursor)
    string += print_tweet(cursor)

    # delete tweet from table tweets by tweet id
    string += 'delete tweet by tweet id %s\n' % tweet_id
    delete_tweets(cursor,'tweet_id',tweet_id)

    # get all tweets
    string += 'get all tweets'+'\n'
    cursor = get_all_tweets(cursor)
    string += print_tweet(cursor)

    # define test tweet
    tweet_id = '908758168733405184'
    people_id = 4

    # insert tweet into table tweets
    string += 'insert tweet %s of user with id %d in table tweets\n' % (tweet_id, people_id)
    insert_tweet(cursor,tweet_id,people_id)

    # define test tweet
    tweet_id = '908392946051026945'
    people_id = 4

    # insert tweet into table tweets
    string += 'insert tweet %s of user with id %d in table tweets\n' % (tweet_id, people_id)
    insert_tweet(cursor,tweet_id,people_id)

    # get all tweets
    string += 'get all tweets'+'\n'
    cursor = get_all_tweets(cursor)
    string += print_tweet(cursor)

    # delete tweet from table tweets by people id
    string += 'delete tweets by user id %s\n' % people_id
    delete_tweets(cursor,'people_id',people_id)

    # get all tweets
    string += 'get all tweets'+'\n'
    cursor = get_all_tweets(cursor)
    string += print_tweet(cursor)

    return string

def main():

    print test_mode()
    
if __name__ == "__main__":
    main()


