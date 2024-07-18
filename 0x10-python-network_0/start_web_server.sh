#!/bin/bash
# This script starts the Flask web server defined in web_0.py

# Kill the existing web server process if web.pid exists
if [ -f web.pid ]; then
    kill -9 $(cat web.pid) > /dev/null 2>&1
    rm web.pid
fi

# Start the new web server process
python3 "$1" > /dev/null 2>&1 &
echo $! > web.pid

# Allow the server time to start
sleep 5

