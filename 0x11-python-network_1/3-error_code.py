#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8) or error code"""
if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
