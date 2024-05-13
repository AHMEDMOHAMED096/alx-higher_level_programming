#!/usr/bin/python3

"""
This script Prints the X-Request-Id header variable of a request to a given URL

Usage: ./1-hbtn_header.py <URL>
"""
from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

with request.urlopen(url) as response:
    headers = response.getheaders()

    for header in headers:
        if header[0] == 'X-Request-Id':
            print(header[1])
