'''6. В одномерном массиве найти сумму элементов, находящихся между
минимальным и максимальным элементами. Сами минимальный и максимальный
элементы в сумму не включать.'''

import random

rand_num = [random.randint(0, 99) for _ in range(10)]
rand_num.sort()
print(f'Массив: {rand_num}')

min_index = 0
max_index = 0
step = 1
difference = 0

for i in rand_num:
    if rand_num[min_index] > i:
        min_index = rand_num.index(i)
    else:
        max_index = rand_num.index(i)

if max_index - min_index < 0:
    step = -1

for i in rand_num[min_index + step:max_index:step]:
    difference += i

print(
        f'Сумма элементов между минимальным ({rand_num[min_index]})',
        f' и максимальным ({rand_num[max_index]}) элементами: {difference}'
        )
