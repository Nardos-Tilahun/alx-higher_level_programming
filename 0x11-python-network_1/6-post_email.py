#!/usr/bin/python3
"""Write a Python script that takes in a URL
sends a POST request to the passed URL
with the email as a parameter, and
finally displays the body of the response."""
from sys import argv
import requests


if __name___ = "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    req = requests.post(url, data=value)

    print(req.text)

