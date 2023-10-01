#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)"""
import sys
import urllib.request
import urllib.parse

url = sys.argv[1]
values = {'email': sys.argv[2]}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    body = response.read()
    print(body.decode('utf-8'))
