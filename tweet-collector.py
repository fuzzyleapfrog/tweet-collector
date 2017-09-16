#!/usr/bin/python

import mysql.connector as mariadb

def print_user(cursor):
    for id, name, twitternick in cursor:
        print("ID: {}, Name: {}, Twitternick: {}").format(id,name,twitternick)    

def get_user(cursor,key,value):
    query = "SELECT id, name, twitternick FROM people WHERE {} = '{}'".format(key,value)
    # alternative query construction
    # query = "SELECT id, name, twitternick FROM people WHERE %s = '%s'" % (key, value)
    cursor.execute(query)
    print_user(cursor)
    return cursor

def get_all_users(cursor):
    cursor.execute("SELECT id, name, twitternick FROM people")
    print_user(cursor)
    return cursor

def insert_user(cursor,name,twitternick):
    query = "INSERT INTO people (id, name, twitternick) VALUES (NULL, '{}', '{}')".format(name,twitternick)
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
name = 'Suzan'

# get one user by twitternick
print 'get one user by twitternick'
cursor = get_user(cursor,'twitternick',twitternick)
# get one user by name
print 'get one user by name'
cursor = get_user(cursor,'name',name)

# get all users
print 'get all users'
cursor = get_all_users(cursor)

# define test user
json_user = {'name': 'test',
             'twitternick': 'testnick'}

# insert user into table people
insert_user(cursor,json_user['name'],json_user['twitternick'])

# get all users
print 'get all users'
cursor = get_all_users(cursor)

# delete user from table people
delete_user(cursor,'name',json_user['name'])

# get all users
print 'get all users'
cursor = get_all_users(cursor)




