#!/usr/bin/python3
"""
This script fetches and displays the 10 most
recent commits of a GitHub repository.
Usage: ./100-github_commits.py <repository_name> <owner_name>
"""

import sys
import requests

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]

    # GitHub API URL to fetch commits
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    # Make a GET request to fetch the commits
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        commits = response.json()
        # Loop through the first 10 commits and print them
        for commit in commits[:10]:
            sha = commit.get("sha")
            author = commit.get("commit", {}).get("author", {}).get("name")
            print(f"{sha}: {author}")
    else:
        print(f"Error: {response.status_code}")
