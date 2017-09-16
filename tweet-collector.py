#!/usr/bin/python

import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='fuzzy', password='leapfrog', database='fuzzy')

cursor = mariadb_connection.cursor()

# get one user by twitternick
cursor.execute("SELECT name,twitternick FROM people WHERE twitternick = %s", ('HeptaSean',))
# print
print 'get one user by twitternick'
for name, twitternick in cursor:
    print("Name: {}, Twitternick: {}").format(name,twitternick)

# get all users
cursor.execute("SELECT name,twitternick FROM people")
# print
print 'get all users'
for name, twitternick in cursor:
    print("Name: {}, Twitternick: {}").format(name,twitternick)

# define test user
json_user = {'name': 'test',
             'twitternick': 'testnick'}

# insert user into table people
cursor.execute("INSERT INTO people (id, name, twitternick) VALUES (NULL, %s, %s)", (json_user['name'],json_user['twitternick']))

# get all users
cursor.execute("SELECT name,twitternick FROM people")
# print
print 'get all users'
for name, twitternick in cursor:
    print("Name: {}, Twitternick: {}").format(name,twitternick)

# delete user from table people
cursor.execute("DELETE FROM people WHERE name = %s", (json_user['name'],))

# get all users
cursor.execute("SELECT name,twitternick FROM people")
# print
print 'get all users'
for name, twitternick in cursor:
    print("Name: {}, Twitternick: {}").format(name,twitternick)


