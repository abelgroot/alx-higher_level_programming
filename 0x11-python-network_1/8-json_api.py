#!/usr/bin/python3
"""
This script takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter. It processes the
JSON response and displays the result.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {"q": letter}

    response = requests.post(url, data=data)

    try:
        json_response = response.json()
        if json_response:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
