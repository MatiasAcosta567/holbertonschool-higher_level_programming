#!/usr/bin/python3
"""Script that takes 2 arguments in order to solve this challenge."""


import requests
from sys import argv


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/" + owner + "/" + repo + "/commits"
    response = requests.get(url)
    commits = response.json()
    for index, elem in enumerate(commits):
        if index <= 9:
            author = elem.get('commit').get('author').get('name')
            code = elem.get('sha')
            print("{}: {}".format(code, author))
        else:
            break
