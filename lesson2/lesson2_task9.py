# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме
# цифр. Вывести на экран это число и сумму его цифр.


def sum_numbers(number):
    summa = 0
    for el in number:
        summa += int(el)
    return summa


list_number = [el for el in input('Введите числа и нажмите Enter: ').split()]

max_number = 0
max_sum = 0
for el in list_number:
    if sum_numbers(el) > max_sum:
        max_number = el
        max_sum = sum_numbers(el)

print(f'У числа {max_number} - наибольшая сумма цифр - {max_sum}')
