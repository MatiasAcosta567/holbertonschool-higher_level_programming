#!/usr/bin/python3
import urllib.request
from sys import argv
"""Script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found
in the header of the response"""


with urllib.request.urlopen(argv[1]) as response:
    info = dict(response.info())
print(info['X-Request-Id'])
