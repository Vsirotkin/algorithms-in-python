
'''9. Найти максимальный элемент среди минимальных элементов столбцов
матрицы.'''

import random

range_num = int(input('введите кол-во столбцов: '))

matrix = []

for i in range(range_num):
    matrix.append([])
    matrix[i].extend([random.randint(0, 99) for _ in range(range_num)])

min_list = []
min_list.extend(matrix[0])

for string in matrix:
    print(('{:4d} ' * len(string)).format(*string))
    i = 0
    for j in string:
        if j < min_list[i]:
            min_list[i] = j
        i += 1

print('-' * 20)
print('min_list')
print(('{:4d} ' * len(min_list)).format(*min_list))

print(
        'Максимальный элемент среди минимальных элементов столбцов матрицы: ',
        min_list[0]
            )
