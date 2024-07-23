#!/bin/zsh

if [ "$#" -ne 1 ]; then
    echo "Usage: is_on.sh host"
    exit 1
fi

ping -c 1 "$1" > /dev/null 2&>1

if [ "$?" -eq 0 ]; then
    echo "OK"
else 
    echo "Host is not reachable"
fi
