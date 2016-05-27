#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

LOCALIP="$(ipconfig getifaddr en0)"
LOCALIP+="$(ipconfig getifaddr en1)"
LOCALIP+="$(ipconfig getifaddr en2)"

echo "Your local IP address: ${LOCALIP}:8000"

echo "=============================="

source $DIR/bin/activate
open http://localhost:8000
$DIR/manage.py runserver 0.0.0.0:8000
