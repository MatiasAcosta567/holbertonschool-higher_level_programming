#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found
in the header of the response"""


import urllib.request
import urllib.parse
import sys


if __name__ = "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read()

    print(page.decode())
