#!/usr/bin/python3
"""
This script fetches the status from
https://alx-intranet.hbtn.io/status using the requests package.
It displays the body of the response in a specific format.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
