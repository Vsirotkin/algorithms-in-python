# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать
# не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное
# пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

'''
1. Сгенерировать случайное число.
2. Ввести счетчик попыток. Присвоить ему значение 1.
3. Пока счетчик попыток меньше, либо равен 10
запрашивать у пользователя очередное число,
    a. если оно больше загаданного, то выводить “много”,
    b. если оно меньше загаданного, то выводить “мало”,
    c. иначе сообщать, что число угадано и прерывать выполнение цикла,
4. увеличивать счетчик попыток на единицу.
5. После цикла, если число не было угадано, то вывести сообщение о том, что попытки исчерпаны,
и какое число было загадано компьютером.
'''
import random


guess_number = round(random.randint(1, 100))
tries = 1
print("Компьютер загадал число от 1 до 20. Отгадайте его. У вас 10 попыток")
while tries <= 100:
    your_number = int(input(f'{tries}-я попытка: '))
    if your_number > guess_number:
        print('Много')
    elif your_number < guess_number:
        print('Мало')
    else:
        print(f'\nВы угадали с {tries}-й попытки!')
        break
    tries += 1
else:
    print(f'\nВы исчерпали 10 попыток. Было загадано {guess_number}.')
    
