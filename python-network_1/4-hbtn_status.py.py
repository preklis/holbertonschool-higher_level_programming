#!/usr/bin/python3
"""Sends a POST request with an email and displays the response body."""

import requests

r=requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.text))