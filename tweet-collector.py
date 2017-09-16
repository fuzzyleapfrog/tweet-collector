#!/usr/bin/python

import mysql.connector as mariadb

def print_user(cursor):
    for name, twitternick in cursor:
        print("ID: {}, Twitternick: {}").format(name,twitternick)    

def get_user(cursor,key,value):
    query = "SELECT id, twitternick FROM people WHERE {} = '{}'".format(key,value)
    cursor.execute(query)
    print_user(cursor)
    return cursor

def get_all_users(cursor):
    cursor.execute("SELECT id, twitternick FROM people")
    print_user(cursor)
    return cursor

def insert_user(cursor,key,value):
    query = "INSERT INTO people (id, {}) VALUES (NULL, '{}')".format(key,value)
    cursor.execute(query)
    print_user(cursor)
    return cursor

def delete_user(cursor,key,value):
    query = "DELETE FROM people WHERE {} = '{}'".format(key,value)
    cursor.execute(query)
    print_user(cursor)
    return cursor

mariadb_connection = mariadb.connect(user='fuzzy', password='leapfrog', database='fuzzy')

cursor = mariadb_connection.cursor()

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
print 'insert user %s' % twitternick
insert_user(cursor,'twitternick',twitternick)

# get all users
print 'get all users'
cursor = get_all_users(cursor)

# delete user from table people
print 'delete user %s' % twitternick
delete_user(cursor,'twitternick',twitternick)

# get all users
print 'get all users'
cursor = get_all_users(cursor)




