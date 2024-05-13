#!/usr/bin/python3
""" Import necessary modules """
import requests
import sys


def get_github_id(username, token):
    """
    This function takes a GitHub username and personal access token as input,
    sends a GET request to the GitHub API and prints the user's id.
    """

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        print(response.json()["id"])
    else:
        print(None)


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    get_github_id(username, token)
