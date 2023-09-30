#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL (with header variable X-School-User-Id set to value 98), and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
