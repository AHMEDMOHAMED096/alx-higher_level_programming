#!/usr/bin/python3
# Import urllib module
from urllib import request


url = 'https://alx-intranet.hbtn.io/status'

with request.urlopen(url) as response:
    body = response.read()

    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
