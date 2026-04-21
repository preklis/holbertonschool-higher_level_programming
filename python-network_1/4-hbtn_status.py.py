#!/usr/bin/python3
"""Sends a POST request with an email and displays the response body."""

import requests

r=requests.get('https://intranet.hbtn.io/status')
print(r.content.decode('utf-8'))