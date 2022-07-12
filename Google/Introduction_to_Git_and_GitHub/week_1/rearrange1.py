#!/usr/bin/env puthon3

import re


def rearrange(name):
    result = re.search(r'^([\w .]*), ([\w .]*)$', name)
    if result == None:
        return result
    return("{} {}".format(result[2], result[1]))


print(rearrange("Ada, Lovel"))
