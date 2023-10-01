#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value
of the 'X-Request-Id' variable found in the header of the response"""
import sys
import urllib.request

url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    print(response.headers['X-Request-Id'])
