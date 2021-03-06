# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

'''
Обычно в языках программирования предусмотрены так называемые логические побитовые операции. О
ни выполняются не над самими числами, а над их двоичным представлением. Например, число 5 в двоичной системе счисления
выражается как 101, а число 6 – как 110. Выполняя логическую побитовую операцию “И” получим число 4, т.к. в младшим
разряде числа 5 стоит 1, а числа 6 – 0. Выражение “1 и 0” возвращает 0. Продолжая поразрядно выполнять логическое “И”
в среднем разряде получим 0, а в старшем 1. Можно записать так:
101
110
100
Двоичное число 100 – это десятичное число 4.

Выполним операцию побитового логического “ИЛИ”:
101
110
111 – это число 7.

“Исключающее ИЛИ”:
101
110
011 – это число 3.

При сдвиге биты просто сдвигаются на указанное количество ячеек в освободившиеся ячейки дописываются нули или единицы
(это зависит от ряда причин):
110 << 2 = 11000 (число 24),
110 >> 2 = 001 (число 1).
'''

a = 5
print("%d = %s" % (a, bin(a)))
b = 6
print("%d = %s" % (b, bin(b)))

print("%d & %d = %d (%s)" % (a ,b , a&b ,bin( a&b)))
print("%d | %d = %d (%s)" % (a ,b , a|b ,bin( a|b)))
print("%d ^ %d = %d (%s)" % (a, b, a^b, bin(a^b)))
print("%d << 2 = %d (%s)" % (a , a<<2 ,bin( a<<2)))
print("%d >> 2 = %d (%s)" % (a , a>>2 ,bin( a>>2)))