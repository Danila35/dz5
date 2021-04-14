"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
from timeit import timeit
from random import randint

enter_num = randint(10000, 1000000)

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num



print(timeit("revers_1(enter_num, revers_num=0)",
                    globals=globals(),
                    number=1000) #-> 0.002721000000000001 (рекурсия)

print(timeit("revers_2(enter_num, revers_num=0)",
                    globals=globals(),
                    number=1000)) #-> 0.0017467999999999997 (цикл)

print(timeit("revers_3(enter_num)",
                    globals=globals(),
                    number=1000)) #-> 0.000570099999999997 (срез) Будет быстрее тк во 1 доказана с помощью таймера во 2 все внутренние функции работают быстрее