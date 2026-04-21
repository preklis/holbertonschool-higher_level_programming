#!/usr/bin/python3
"""Lists 10 commits of a GitHub repository."""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    r = requests.get(url)

    try:
        commits = r.json()

        for commit in commits[:10]:
            sha = commit.get("sha")
            name = commit.get("commit", {}).get("author", {}).get("name")
            print(f"{sha}: {name}")

    except ValueError:
        pass
