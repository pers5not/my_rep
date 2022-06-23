# Функция group_list принимает имя группы и список участников и возвращает строку в формате: group_name: member1, member2, … Например, group_list("g", ["a", "b", "c"]) возвращает "g: a, b, c". Заполните пробелы в этой функции, чтобы сделать это.

def group_list(group, users):
    members = ', '.join(users)
    return f"{group}: {members}"

    # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))
# Should be "Engineering: Kim, Jay, Tom"
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))
print(group_list("Users", ""))  # Should be "Users:"
