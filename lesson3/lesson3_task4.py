'''4. Определить, какое число в массиве встречается чаще всего.'''

from random import random
num_range = 5
amount_num = 20
num_list = [int(random()*num_range) for i in range(amount_num)]
num_list.sort()
print(f'исходный список: {num_list}')

max_frequent = num_list[0]
max_count = num_list.count(max_frequent)
for el in num_list:
    if num_list.count(el) > max_count:
        max_frequent = el
        max_count = num_list.count(el)
print(f'наиболее частая цифра: {max_frequent} - встречается {max_count} раз.')
