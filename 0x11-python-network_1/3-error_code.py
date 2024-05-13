#!/usr/bin/python3
""" Import necessary modules """
import sys
from urllib import request, error


def send_request(url):
    """
    This function takes a URL as input, sends a request to the URL
    and prints the body of the response If an HTTP error occurs,
    it catches the exception and prints the error code.
    """

    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    url = sys.argv[1]
    send_request(url)
