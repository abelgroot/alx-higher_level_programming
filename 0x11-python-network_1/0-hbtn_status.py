#!/usr/bin/python3
"""
This script fetches the status from
https://alx-intranet.hbtn.io/status using the urllib package.
It displays the body of the response in a specific format.
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
