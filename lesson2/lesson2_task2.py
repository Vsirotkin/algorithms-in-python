# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

'''
1. Присвоить переменным-счетчикам четных (even) и нечетных (odd) цифр значение 0.
2. Пока введенное число не уменьшится до нуля выполнять нижеследующие действия:
3. Если число четное (делится нацело на 2), значит последняя его цифра четная и надо увеличить на 1 переменную even.
4. Иначе число нечетное и следует добавить 1 к переменной odd.
5. Убрать последнюю цифру числа путем деления числа нацело на 10.
'''

num = input('Введите любое целое число: ')
even = odd = 0
even_list = []
uneven_list = []

num = int(num)
while num > 0:
    num = str(num)
    for el in num:
        el = int(el)
        if el % 2 == 0:
            even_list.append(el)
            num = int(num)
            even += 1
        else:
            uneven_list.append(el)
            num = int(num)
            odd += 1
        num = num // 10
print(f'В введоенном числе:\nкол-во цифр {even + odd},\nчетных цифры {even} {even_list},\nнечетных цифр {odd} {uneven_list}')
