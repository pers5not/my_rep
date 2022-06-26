import imp


import shutil
from termcolor import colored, cprint


du = shutil.disk_usage("/")

cprint(du.free/du.total * 100,)
