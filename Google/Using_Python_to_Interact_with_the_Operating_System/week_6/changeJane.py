#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1], 'r') as file:
    for line in file.readlines():
        line = line.strip()
        new_name = line.replace('jane', 'jdoe')
        subprocess.run(['mv', line, new_name])

file.close()
