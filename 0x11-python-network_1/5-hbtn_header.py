#!/usr/bin/python3
""" Import necessary modules """
import requests
import sys


def get_header_x_request_id(url):
    """
    This function takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the response.
    """

    response = requests.get(url)
    _headers = response.headers
    if "X-Request-Id" in _headers:
        print(_headers["X-Request-Id"])


if __name__ == "__main__":
    url = sys.argv[1]
    get_header_x_request_id(url)
