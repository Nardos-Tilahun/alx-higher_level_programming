#!/usr/bin/python3
"""Write a Python script that fetches
https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    req = request.get("https://alx-intranet.hbtn.io/status")
    print("Body Response:")
    print("\t- type: {}"format(type(req.text)))
    print("\t- content: {}"format(req.text))
