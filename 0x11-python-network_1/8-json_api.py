#!/usr/bin/python3
""" Import necessary modules """
import requests
import sys


def send_request(url, letter):
    """
    This function takes in a letter and sends a POST request
    with the letter as a parameter.
    """

    response = requests.post(url, data={"q": letter})
    try:
        r_dict = response.json()
        if len(r_dict) == 0:
            print("No result")
        else:
            print(f'[{r_dict["id"]}] {r_dict["name"]}')
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(sys.argv) < 2 else sys.argv[1]
    send_request(url, letter)
