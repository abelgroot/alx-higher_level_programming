#!/bin/bash
# Sends a GET request to a URL and displays the body of the response if the status is 200
curl -s -X GET "$1" -o /dev/stdout -w "%{http_code}" | sed '$ d'
