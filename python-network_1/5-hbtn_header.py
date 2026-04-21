#!/usr/bin/python3
"""Sends a POST request with an email and displays the response body."""

import requests
import sys
url = sys.argv[1]
r = requests.get(url)
print(r.headers.get('X-Request-Id'))

