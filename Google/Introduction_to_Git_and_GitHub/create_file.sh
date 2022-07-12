#!/bin/bash 

comand=$1
echo '#!/usr/bin/env python3' > $comand| chmod +x $comand | code $comand
