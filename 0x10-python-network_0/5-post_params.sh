#!/bin/bash
#  takes in a URL, sends a POST request to the passed URL (with variable 'email' set to 'test@gmail.com' and variable 'subject' set to 'I will always be here for PLD'), and displays the body of the response
curl -sX POST -d email=test%40gmail%2Ecom -d subject=I+will+always+be+here+for+PLD "$1"
