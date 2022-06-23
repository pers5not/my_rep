# Функция is_palindrome проверяет, является ли строка палиндромом. Палиндром — это строка, которую можно одинаково читать как слева направо, так и справа налево, пропуская пробелы и игнорируя заглавные буквы. Примерами палиндромов являются такие слова, как каяк и радар, а также такие фразы, как «Никогда нечетное или четное». Заполните пробелы в этой функции, чтобы вернуть True, если переданная строка является палиндромом, и False, если нет.

# def is_palindrome(input_string):
#     input_string_1 = input_string[::-1].lower().replace(' ', '')
#     if input_string_1 == input_string.lower().replace(" ", ""):
#         return True
#     else:
#         return False


# print(is_palindrome("Never Odd or Even"))  # Should be True
# print(is_palindrome("abc"))  # Should be False
# print(is_palindrome("kayak"))  # Should be True


def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for let in input_string:
        if let != " ":
            new_string += let
            reverse_string = let + reverse_string
    # Compare the strings
    if reverse_string.lower() == new_string.lower():
        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True
