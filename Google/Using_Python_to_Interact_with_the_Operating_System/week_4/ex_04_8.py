#!/usr/bin/env python 3
import sys
logfile = sys.argv[1]
with open('logfile') as f:
    for line in f:
        f.write(line.strip())
