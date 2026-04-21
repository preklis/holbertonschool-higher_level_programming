#!/usr/bin/python3
"""Fetches GitHub user ID using Basic Authentication."""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    r = requests.get(
        "https://api.github.com/user",
        auth=(username, token)
    )

    try:
        data = r.json()
        print(data.get("id"))
    except ValueError:
        print("None")
