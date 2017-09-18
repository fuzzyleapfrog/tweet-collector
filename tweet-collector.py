#!/usr/bin/python

from wsgiref.simple_server import make_server
import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import tweet_collector_website as website

def application (environ,start_response):
    response_body = website.startpage().encode('utf-8')
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


