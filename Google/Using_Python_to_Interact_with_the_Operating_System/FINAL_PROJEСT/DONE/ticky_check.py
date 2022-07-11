#!/usr/bin/env python3

import re
import csv
import operator
from tokenize import group

dict_errors = {}
dict_infos = {}

with open('syslog.log', 'r') as log_file:
    for line in log_file:
        match = re.search(
            r"ticky: ([\w+]*) ([\w' ]*)[\[#\d]*\]?]? \((.*)\)$", line.strip())
        code, error_msg, user = match.group(1), match.group(2), match.group(3)
        if user not in dict_infos.keys():
            dict_infos[user] = {}
            dict_infos[user]['ERROR'] = 0
            dict_infos[user]['INFO'] = 0
        if code == 'INFO':
            dict_infos[user]['INFO'] += 1
        elif code == 'ERROR':
            dict_errors[error_msg] = dict_errors.get(error_msg, 0) + 1
            dict_infos[user]['ERROR'] += 1

errors_list = sorted(dict_errors.items(),
                     key=operator.itemgetter(1), reverse=True)

infos_list = sorted(dict_infos.items(), key=operator.itemgetter(0))

log_file.close()

errors_list.insert(0, ('Error', 'Count'))
infos_list.insert(0, ('Username', {'INFO': 'INFO', 'ERROR': 'ERROR'}))
print(infos_list)

with open('user_statistics.csv', 'w') as user_csv:
    for k, v in infos_list:
        user_csv.write(str(k) + ',' +
                       str(v['INFO']) + ',' + str(v['ERROR'])+'\n')
user_csv.close()

with open('error_message.csv', 'w') as error_csv:
    for k, v in errors_list:
        error_csv.write(str(k) + ',' + str(v)+'\n')
error_csv.close
