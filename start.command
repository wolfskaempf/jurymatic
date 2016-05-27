#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Your local IP address:"
ipconfig getifaddr en0
ipconfig getifaddr en1
ipconfig getifaddr en2

echo "=============================="

source $DIR/bin/activate
$DIR/manage.py runserver 0.0.0.0:8000
