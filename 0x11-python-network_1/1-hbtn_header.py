#!/usr/bin/python3
import urllib.request
import sys
"""Script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found
in the header of the response"""


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
       info = response.getheader("X-Request-Id")
    print(info)