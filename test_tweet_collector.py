#!/usr/bin/python

import ConfigParser
import mysql.connector as mariadb
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from database import *

def teststring():

    connection, cursor = connect_to_db()

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

    # get latest users
    string += 'get latest users'+'\n'
    cursor = get_latest_users(cursor)
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

    # get latest tweets
    string += 'get latest tweets'+'\n'
    cursor = get_latest_tweets(cursor)
    string += print_latest_tweets(cursor)

    # ---- URL ----
    
    # define broken url
    url = 'https://www.twitter.com/FuzzyLeapfrog/status/877880899764977664'

    # check url
    string += 'check broken url'+'\n'
    dict = check_url(url)
    if 'twitternick' in dict:
        for key in dict:
            string += key+': '+dict[key]+'\n'
    else:
        string += 'Extracting twitternick and tweet_id failed.'+'\n'

    # define valid url
    url = 'https://twitter.com/FuzzyLeapfrog/status/877880899764977664'

    # check url
    string += 'check valid url'+'\n'
    dict = check_url(url)
    if 'twitternick' in dict:
        for key in dict:
            string += key+': '+dict[key]+'\n'
    else:
        string += 'Extracting twitternick and tweet_id failed.'+'\n'

#   ---

    # define already existing user and tweet
    url = 'https://twitter.com/FuzzyLeapfrog/status/877880899764977664'

    # check whether user is already in database
    string += 'url with user already in database'+'\n'
    # TODO
    
#   ---

    # define not already existing tweet but user
    url = 'https://twitter.com/FuzzyLeapfrog/status/911338177323048960'

    # check whether user is already in database
    string += 'url with user already in database'+'\n'
    # TODO

    # get all users
    string += 'get all users'+'\n'
#    cursor = get_all_users(cursor)
#    string += print_user(cursor)

    # check whether tweet is already in database, if not, insert
    string += 'url with tweet not already in database'+'\n'
#   TODO

    # get all tweets
    string += 'get all tweets'+'\n'
#    cursor = get_all_tweets(cursor)
#    string += print_tweet(cursor)

    # delete tweet from table tweets by tweet id
    string += 'delete tweet by tweet id 911338177323048960\n'
#    delete_tweets(cursor,'tweet_id','911338177323048960')

    # get all tweets
    string += 'get all tweets'+'\n'
#    cursor = get_all_tweets(cursor)
#    string += print_tweet(cursor)

#   ---

    # define not already existing user and tweet
    url = 'https://twitter.com/BMittermaier/status/911289262783557633'

    # check whether user is already in database, if not, insert
    string += 'url with user not already in database'+'\n'
    # TODO
    
    # get all users
    string += 'get all users'+'\n'
#    cursor = get_all_users(cursor)
#    string += print_user(cursor)

    # delete user from table people
    string += 'delete user BMittermaier\n'
#    delete_user(cursor,'twitternick','BMittermaier')

    # get all users
    string += 'get all users'+'\n'
#    cursor = get_all_users(cursor)
#    string += print_user(cursor)

    # check whether tweet is already in database, if not, insert
    string += 'url with tweet not already in database'+'\n'
#    TODO

    # get all tweets
    string += 'get all tweets'+'\n'
#    cursor = get_all_tweets(cursor)
#    string += print_tweet(cursor)

    # delete tweet from table tweets by tweet id
    string += 'delete tweet by tweet id 911289262783557633\n'
#    delete_tweets(cursor,'tweet_id',tweet_id)

    # get all tweets
    string += 'get all tweets'+'\n'
#    cursor = get_all_tweets(cursor)
#    string += print_tweet(cursor)

    return string

def main():

    print teststring()
    
if __name__ == "__main__":
    main()


