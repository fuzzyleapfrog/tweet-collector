#!/usr/bin/python

from wsgiref.simple_server import make_server
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import test_tweet_collector as test

def application (environ,start_response):
    response_body = test.teststring()
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
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


