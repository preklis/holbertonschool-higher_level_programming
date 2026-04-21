#!/usr/bin/python3
"""Sends a POST request with an email and displays the response body."""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().deocde('utf-8')
            print(body)

    except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
