#!/usr/bin/env python3

import psutil
from termcolor import colored, cprint
import shutil


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    return psutil.cpu_percent(1) < 75


if not check_disk_usage("/") or not check_cpu_usage():
    cprint("ERROR!!!", 'red')
else:
    cprint("Everything is OK!", 'magenta', attrs=['bold'])
