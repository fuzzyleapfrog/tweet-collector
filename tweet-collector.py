#!/usr/bin/python

from wsgiref.simple_server import make_server
import sys, os
from cgi import parse_qs
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import tweet_collector_website as website
import database

def application (environ,start_response):
    query = parse_qs(environ['QUERY_STRING'])
    url = ""
    if "url" in query:
        url = query["url"][0] # assume one url as input
    # TODO: call database to check if the user of the tweet is already in the database and,
    #       if not, to insert the user. Check also whether the tweet is already in the
    #       database and, if not, insert the tweet into the database.
    # TODO: Reload list of recently entered users/tweets.
    response_body = website.startpage(url).encode('utf-8')
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)
    return [response_body]

def main():

    # start program and go to localhost:8051 in browser
    httpd = make_server (
        'localhost',
        8051,
        application 
    )
    #httpd.handle_request()
    httpd.serve_forever()

if __name__ == "__main__":
    main()


