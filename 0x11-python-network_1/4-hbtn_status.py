#!/usr/bin/python3
""" Import necessary modules """
import requests

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)
print("Body response:")
print("\t- type: {}".format(type(url)))
print("\t- content: {}".format(response.content))
