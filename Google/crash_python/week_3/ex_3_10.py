# Функция count_users рекурсивно подсчитывает количество пользователей, принадлежащих к группе в системе компании, просматривая каждого из членов группы и, если один из них является группой, рекурсивно вызывая функцию и подсчитывая членов. Но у него есть ошибка! Сможете ли вы обнаружить проблему и устранить ее?
def count_users(group):
    count = 0
    for member in get_members(group):
        count += 1
        if is_group(member):
            count += count_users(member)-1
    return count


print(count_users("sales"))  # Should be 3
print(count_users("engineering"))  # Should be 8
print(count_users("everyone"))  # Should be 18
