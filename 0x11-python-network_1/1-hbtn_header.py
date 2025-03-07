#!/usr/bin/python3
"""
This script takes a URL as input,
sends a request to the URL, and displays the value of the
X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get("X-Request-Id")
        print(x_request_id)
