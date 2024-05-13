#!/usr/bin/python3
""" Import necessary modules """
import requests
import sys


def send_post_request(url, email):
    """
    This function takes a URL and an email as input and
    sends a POST request to the URLwith the email as a parameter
    and prints the body of the response.
    """

    response = requests.post(url, data={"email": email})
    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
