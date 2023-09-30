#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response if it's status code is 200(success)
curl -sfL -X GET "$1"
