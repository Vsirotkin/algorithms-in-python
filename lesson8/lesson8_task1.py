"""1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке."""

import hashlib

user_text = input('Введите строку, состоящую только из маленьких латинских букв: ')

sum_subuser_text = set()

for i in range(len(user_text)):
    for j in range(len(user_text), i, -1):
        hash_str = hashlib.sha1(user_text[i:j].encode('utf-8')).hexdigest()
        sum_subuser_text.add(hash_str)

print(f'{len(sum_subuser_text) -1} различных подстрок в строке {user_text}')
