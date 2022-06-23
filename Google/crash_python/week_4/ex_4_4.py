# Функция replace_ending заменяет старую строку в предложении новой строкой, но только если предложение заканчивается старой строкой. Если старая строка встречается в предложении более одного раза, заменяется только последняя строка, а не все. Например, replace_ending("abcabc", "abc", "xyz") должен возвращать abcxyz, а не xyzxyz или xyzabc. Сравнение строк чувствительно к регистру, поэтому replace_ending("abcabc", "ABC", "xyz") должен возвращать abcabc (без изменений).

def replace_ending(sentence, old, new):
    if sentence.endswith(old):
        i = sentence.split()
        i[-1] = new
        new_sentence = ' '.join(i)
        return new_sentence
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"
