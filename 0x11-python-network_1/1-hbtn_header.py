#!/usr/bin/python3
""" module that display the value of the X-request-Id variable found in the header of the response from the URL given"""
from sys import argv
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)
    
    with urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
