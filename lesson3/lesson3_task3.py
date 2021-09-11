'''3. В массиве случайных целых чисел поменять местами минимальный и
максимальный элементы.'''

import random

rand_num = [random.randint(0, 99) for _ in range(10)]
print(f'Массив до изменения: {rand_num}')

max_num = rand_num[0]
min_num = rand_num[0]

for i in rand_num:
    if i > max_num:
        max_num = i
    else:
        min_num = i
min_index = rand_num.index(min_num)
max_index = rand_num.index(max_num)
rand_num[min_index], rand_num[max_index] = rand_num[max_index], rand_num[min_index]
print(f'Массив осле изменения мест элементов {min_index} и {max_index}: {rand_num}')
