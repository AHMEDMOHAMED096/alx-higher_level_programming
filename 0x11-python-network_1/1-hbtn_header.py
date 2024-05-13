#!/usr/bin/python3
""" Import urllib module and
sys module
"""
from urllib import request
import sys


url = sys.argv[1]

with request.urlopen(url) as response:
    headers = response.getheaders()

    for header in headers:
        if header[0] == 'X-Request-Id':
            print(header[1])
