LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWEL_COST = 250
VOWELS = 'AEIOU'
prizeMoney = 0
guessed = ['A', 'B', 'C']

possible_letters = []
impossible_letters = []
if prizeMoney < VOWEL_COST:
    for vowel in VOWELS:
        impossible_letters.append(vowel)
    impossible_letters += guessed
else:
    impossible_letters = guessed
for letter in LETTERS:
    if letter not in impossible_letters:
        possible_letters += letter
print(impossible_letters)
print(possible_letters)
