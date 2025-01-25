#!/usr/bin/python3
"""
This script uses the GitHub API to display the user's GitHub ID.
The username and personal access token are passed as command-line arguments.
"""

import sys
import requests

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API endpoint for user information
    url = "https://api.github.com/user"

    # Send a GET request with Basic Authentication
    response = requests.get(url, auth=(username, token))

    # Parse the JSON response
    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print(None)
