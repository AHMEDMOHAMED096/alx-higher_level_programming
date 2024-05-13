#!/usr/bin/python3
# # Import necessary modules
import sys
from urllib import request, parse


def send_post_request(url, email):
    """
    This function takes a URL and an email as input and
    sends a POST request to the URLwith the email as a parameter
    and prints the body of the response.
    """

    data = parse.urlencode({'email': email}).encode()
    req = request.Request(url, data=data)

    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
