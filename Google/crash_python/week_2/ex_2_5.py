# Если файловая система имеет размер блока 4096 байт, это означает, что файл, состоящий только из одного байта, по-прежнему будет использовать 4096 байт памяти. Файл, состоящий из 4097 байт, будет использовать 4096*2=8192 байта памяти. Зная это, можете ли вы заполнить пробелы в приведенной ниже функции calculate_storage, которая вычисляет общее количество байтов, необходимых для хранения файла заданного размера?

def calculate_storage(filesize):
    block_size = 4096
    full_blocks = filesize // block_size
    partial_block_remainder = filesize % block_size
    if partial_block_remainder > 0:
        return block_size+full_blocks*block_size
    return block_size


print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192
