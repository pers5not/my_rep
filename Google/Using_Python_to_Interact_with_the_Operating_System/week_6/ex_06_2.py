#!/usr/bin/env python3

import sys

for line in sys.stdin:
    print(line.strip().upper())


# cat haiku.txt | ./ex_06_2.py
# ./ex_06_2.py < haiku.txt
