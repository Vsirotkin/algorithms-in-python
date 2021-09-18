'''8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних
элементов строк. Программа должна вычислять сумму введенных элементов
каждой строки и записывать в последнюю ячейку строки. В конце следует
вывести полученную матрицу.'''


matrix = []

for i in range(4):
    matrix.append([])
    sum_num = 0
    for el in range(4):
        user_number = int(input(f'Введите элемент {i+1} и {el+1} столбца: '))
        sum_num += user_number
        matrix[i].append(user_number)

    matrix[i].append(sum_num)

for el in matrix:
    print(('{:>4d}' * 5).format(*el))
