#!/usr/bin/python3
"""Sends a POST request and handles JSON response."""

import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    r = requests.post(
        "http://0.0.0.0:5000/search_user",
        data={"q": q}
    )

    try:
        data = r.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit()

    if not data:
        print("No result")
    else:
        print(f"[{data.get('id')}] {data.get('name')}")
