# Функция transform_comments преобразует комментарии в скрипте Python в комментарии, используемые компилятором C. Это означает поиск текста, начинающегося с решётки (#), и замену его двойной косой чертой (//), что является индикатором однострочного комментария C. В этом упражнении мы проигнорируем возможность использования решётки, встроенной в команду Python, и предположим, что она используется только для обозначения комментария. Мы также хотим рассматривать повторяющиеся знаки решетки (##), (###) и т. д. как один индикатор комментария, который нужно заменять только (//), а не (#//) или (//#) . Заполните параметры метода подстановки, чтобы выполнить эту функцию:

import re


def transform_comments(line_of_code):
    result = re.sub(r'#{1,}', '//', line_of_code)
    return result


print(transform_comments("### Start of program"))
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable"))
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable"))
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)"))
# Should be "  return(number)"
