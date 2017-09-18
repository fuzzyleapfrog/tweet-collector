#!/usr/bin/python

import jinja2
import os

def startpage():

    currentpath = os.path.dirname(__file__)

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(currentpath),
    )

    template = env.get_template('tweet_collector_website.html')

    list = [{'user1': 'User1'},
            {'user2': 'User2'},
            {'user3': 'User3'}]
    
    return template.render(l=list)

def main():
    print startpage()

if __name__ == "__main__":
    main()


