#!/usr/bin/python3
"""
This script retrieves and prints the 'X-Request-Id'
from the headers of a given URL.

The URL is passed as a command-line argument to the script.
Usage: ./1-hbtn_header.py URL
"""

# Import necessary modules
from urllib import request
import sys


url = sys.argv[1]

with request.urlopen(url) as response:
    headers = response.getheaders()

    for header in headers:
        if header[0] == 'X-Request-Id':
            print(header[1])
