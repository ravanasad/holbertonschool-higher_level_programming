#!/usr/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 invalid"
    exit 1
fi

if [ -z "$2" ]; then
    cat $1 | mysql -u root hbtn_0c_0 
else
    cat $1 | mysql -hlocalhost -u root $2 
fi
