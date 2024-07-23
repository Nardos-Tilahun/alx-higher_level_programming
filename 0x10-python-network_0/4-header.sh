#!/bin/bash
#Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -sL "$1" -H "X-School-User-Id: 98"
