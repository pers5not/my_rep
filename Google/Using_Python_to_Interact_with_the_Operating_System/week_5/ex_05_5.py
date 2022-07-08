#!/usr/bin/env python3
def character_frequency(file_name):
    try:
        f = open(file_name)
    except OSError:
        return None

    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters


print(character_frequency('test.txt'))
