
'''7. В одномерном массиве целых чисел определить два наименьших
элемента. Они могут быть как равны между собой (оба являться
минимальными), так и различаться.'''

import random

rand_num = [random.randint(0, 99) for _ in range(10)]
rand_num.sort()
print(f'Массив: {rand_num}')

sort_list = []
sort_list.extend(rand_num)

print(
    f'Два наименьших элемента (через сортировку): {sort_list[0]} и {sort_list[1]}'
    )
