# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он:
# разносторонним,
# равнобедренным или
# равносторонним.

'''
Треугольник существует только тогда, когда сумма длин любых его двух сторон больше третьей стороны.
Иначе две стороны просто “укладываются” на третьей.
Треугольник является разносторонним, если все его стороны имеют разную длину; треугольник будет равнобедренным,
если любые две его стороны равны между собой, но отличны от третьей; и треугольник является равносторонним,
когда все его стороны равны.
Прежде чем выяснять вид треугольника, необходимо удостовериться, что треугольник существует.

Если треугольник существует, то можно сначала проверить на неравенство три его стороны.
Если они не равны друг другу, то треугольник разносторонний. Если это не так,
то следующим шагом будет проверка на равенство всех сторон треугольника. Если все стороны равны,
делается вывод о том, что треугольник равносторонний. Иначе остается только один вариант – равнобедренный треугольник.
'''

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существует")
elif a != b and a != c and b != c:
    print("Разносторонний")
elif a == b == c:
    print("Равносторонний")
else:
    print("Равнобедренный")
