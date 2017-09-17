#!/usr/bin/python

import jinja2
import os

currentpath = os.path.dirname(__file__)

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(currentpath),
)

template = env.get_template('website.html')

print template.render(user1='User1', user2='User2')

