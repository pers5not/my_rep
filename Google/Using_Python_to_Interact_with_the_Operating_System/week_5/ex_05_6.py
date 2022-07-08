def validate_user_name(user_name, minlen):
    assert type(user_name) == str, "username must be at sring"
    if minlen < 1:
        raise ValueError('minlen must be at least 1')
    if len(user_name) < minlen:
        return False
    if not user_name.isalnum():
        return False
    return True


# print(validate_user_name("Alex", 1))
# print(validate_user_name([], 1))
# print(validate_user_name(5, 1))
# validate_user_name("", 0)
