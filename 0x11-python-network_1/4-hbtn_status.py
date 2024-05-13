#!/usr/bin/python3
""" Import necessary modules """
import requests

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)
content = response.text
print("Body response:")
print("\t- type: {}".format(type(content)))
print("\t- content: {}".format(content))
