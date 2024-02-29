#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
curl -sIX OPTIONS "$1" | grep -i 'Allow' | awk '{print substr($0, 8)}'
