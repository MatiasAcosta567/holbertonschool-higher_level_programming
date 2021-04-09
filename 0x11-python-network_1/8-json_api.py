#!/usr/bin/python3
"""Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter"""


import requests
from sys import argv


if __name__ == "__main__":
    data = {"q": argv[1] if len(argv) == 2 else ""}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=data)
    try:
        json_resp = response.json()
        if len(json_resp) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json_resp.get("id"), json_resp.get("name")))
    except:
        print("Not a valid JSON")
