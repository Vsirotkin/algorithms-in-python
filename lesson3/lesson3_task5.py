'''5. В массиве найти максимальный отрицательный элемент. Вывести на
экран его значение и позицию в массиве.'''

import random

rand_num = [random.randint(-99, 99) for _ in range(10)]
print(f'Массив: {rand_num}')

min_index = 0
for i in rand_num:
    if rand_num[min_index] > i:
        min_index = rand_num.index(i)

if rand_num[min_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве минимальный отрицательный элемент: {rand_num[min_index]}.',
            f'Находится в массиве на позиции {min_index}')
