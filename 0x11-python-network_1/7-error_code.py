#!/usr/bin/python3
""" Import necessary modules """
import requests
import sys


def send_request(url):
    """
    This function takes a URL as input, sends a request to the URL
    and prints the body of the response If an HTTP error occurs,
    it prints the error code.
    """

    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")


if __name__ == "__main__":
    url = sys.argv[1]
    send_request(url)
