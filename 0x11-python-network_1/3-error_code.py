#!/usr/bin/python3
"""
This script takes a URL as input,sends a request
to the URL, and displays the body of the
response (decoded in utf-8). If an HTTP error occurs, it prints the error code.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
