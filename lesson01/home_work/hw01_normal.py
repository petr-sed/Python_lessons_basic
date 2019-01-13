
__author__ = 'Sedukin Petr'
import math

def inp_var(intro_long, intro_short, int_float):
    if intro_long == 0:
        vr = int_float(input('Укажите значение переменной ' + intro_short + ': '))
    elif intro_short == 0:
        vr = int_float(input(intro_long))
    else:
        vr = int_float(input(intro_long + ' ' + intro_short + ': '))
    return vr

def number_splitter(numb_loc):
    mass_numb = []
    i_loc = 0
    while numb_loc > 0:
        mass_numb.insert(-i_loc, numb_loc%10)
        numb_loc = numb_loc//10
        i_loc = i_loc+1
    return mass_numb

def part_hw_choose():
    part_hw = inp_var("Выберите часть ДЗ (1, 2, 3): ", 0, int)
    if part_hw == 1:
        part_1()
    elif part_hw == 2:
        part_2()
    elif part_hw == 3:
        part_3()
    else:
        print('Нет такого варианта.')
    return input('Хотите продолжит? Y/N:')

def part_1():
    # Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
    # Например, дается x = 58375.
    # Нужно вывести максимальную цифру в данном числе, т.е. 8.
    # Подразумевается, что мы не знаем это число заранее.
    # Число приходит в виде целого беззнакового.
    # Подсказки:
    # * постарайтесь решить задачу с применением арифметики и цикла while;
    # * при желании и понимании решите задачу с применением цикла for.
    number = inp_var('Укажите произвольное число: ', 0, int)
    mass = number_splitter(number)
    l = len(mass)
    a = 0
    for i in range(l):
        if a < mass[i]:
            a = mass[i]
    print('Самая большая цифра числа', number)
    print('Это', a)

def part_2():
    # Задача-2: Исходные значения двух переменных запросить у пользователя.
    # Поменять значения переменных местами. Вывести новые значения на экран.
    # Решите задачу, используя только две переменные.
    # Подсказки:
    # * постарайтесь сделать решение через действия над числами;
    # * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
    a = inp_var(0, 'a', int)
    b = inp_var(0, 'b', int)
    a = a+b
    b = a-b
    a = a-b
    print("Значение переменной a равно:", a)
    print("Значение переменной b равно:", b)

def part_3():
    # Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
    # ax² + bx + c = 0.
    # Коэффициенты уравнения вводятся пользователем.
    # Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
    # import math
    # math.sqrt(4) - вычисляет корень числа 4
    a = inp_var(0, 'a', float)
    b = inp_var(0, 'b', float)
    c = inp_var(0, 'c', float)
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b+math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2*a)
        print('Квадратное уравнение', a, '* x * x +', b, '* x +', c, '= 0 имеет два корня:')
        print('x1 =', x1)
        print('x2 =', x2)
    elif d == 0:
        x1 = -b/(2*a)
        print('Квадратное уравнение', a, '* x * x +', b, '* x +', c, '= 0 имеет один корень:')
        print('x =', x1)
    else:
        print('Квадратное уравнение', a, '* x* x +', b, '* x +', c, '= 0 не имеет корней')

answer = 'Y'
while answer == 'Y' or answer == 'y':
    answer = part_hw_choose()
print("Вы закончили проверять мое домашнее задание, спасибо!")