#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
    echo "Everything Ok"
else
    echo "ERROR! 127.0.0.1 is not in /etc/hosts"

fi


# if test -n "$PATH"; then echo "path is not empty"; fi
