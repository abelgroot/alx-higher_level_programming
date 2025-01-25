#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument with a file's content as the request body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
