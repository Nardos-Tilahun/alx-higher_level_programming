#!/bin/bash
# This script takes a URL, sends a request, and displays the size of the response body in bytes

size=$(curl -s "$1" | wc -c)
echo "$size"

