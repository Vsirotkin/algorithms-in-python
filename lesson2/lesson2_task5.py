# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

'''
Для чисел от 32 до 127 выводить их на экран,
получать соответствующий им символ из таблицы кодов ASCII и также выводить его на экран.

После каждого 10-го символа переходить на новую строку.
'''

for el in range(32, 128):
    print("%4d-%s" % (el, chr(el)), end='')
    if el % 10 == 0:
        print()
