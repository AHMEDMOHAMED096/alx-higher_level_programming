# Import required modules
import urllib.request
import urllib.parse
import sys


url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode()

request = urllib.request.Request(url, data=data)

with urllib.request.urlopen(request) as response:
    body = response.read().decode('utf-8')

    print(f'Your email is: {body}')
