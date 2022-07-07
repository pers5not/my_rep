
# print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )

# print(sum([(line) for line in re.findall('[0-9]+', handle.read())]))


import re
handle = open(f"ex_11_01/regex_sum_1543578.txt", "r")
my_list = list()
for line in handle:
    lst_num = re.findall('[0-9]+', line)
    if len(lst_num) == 0:
        continue
    for num in lst_num:
        my_list.append(int(num))
print(sum(my_list))
