#!/usr/bin/env python3

import os
import sys

file_name = sys.argv[1]
if not os.path.exists(file_name):
    with open(file_name, 'w') as file:
        file.write("New file created\n")
else:
    print(f"Error the file {file_name} alredy exists")
    sys.exit(1)
