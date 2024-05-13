#!/usr/bin/python3
""" Import necessary modules """
import sys
from urllib import request


def get_header_x_request_id(url):
    """
    This function takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the response.
    """

    with request.urlopen(url) as response:
        headers = response.getheaders()
        for header in headers:
            if header[0] == 'X-Request-Id':
                print(header[1])


if __name__ == "__main__":
    url = sys.argv[1]
    get_header_x_request_id(url)
