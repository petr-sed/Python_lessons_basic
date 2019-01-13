
__author__ = 'Sedukhin Petr'

def number_splitter(number):
    mass_numb = []
    i = 0
    while number > 0:
        mass_numb.insert(-i, number%10)
        number = number//10
        i = i+1
    return mass_numb


def inp_var(intro_long, intro_short):
    if intro_long == 0:
        vr = int(input('Укажите значение переменной ' + intro_short + ': '))
    elif intro_short == 0:
        vr = int(input(intro_long))
    else:
        vr = int(input(intro_long + ' ' + intro_short + ': '))
    return vr

def part_hw_choose():
        part_hw = inp_var("Выберите часть ДЗ (1, 2, 3):", 0)
        if part_hw == 1:
            part_1()
        elif part_hw == 2:
            part_2()
        elif part_hw == 3:
            part_3()
        else:
            print('Нет такого варианта.')
        return input('Хотите продолжит? Y/N:')


def part_1 ():
    # Задача-1: Дано произвольное целое число (число заранее неизвестно).
    # Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
    # Подсказки:
    # * постарайтесь решить задачу с применением арифметики и цикла while;
    # * при желании решите задачу с применением цикла for.
    user_number = inp_var('Введите произвольное число:', 0)
    print('Введеное число:', user_number)
    print('Состоит из цифр:')
    mass = number_splitter(user_number)
    l = len(mass)
    for i in range(l):
        print(mass[i])


def part_2():
    # Задача-2: Исходные значения двух переменных запросить у пользователя.
    # Поменять значения переменных местами. Вывести новые значения на экран.
    # Подсказка:
    # * постарайтесь сделать решение через дополнительную переменную
    #   или через арифметические действия
    # Не нужно решать задачу так:
    # print("a = ", b, "b = ", a) - это неправильное решение!
    a = inp_var(0, 'a')
    b = inp_var(0, 'b')
    c = a + b
    a = c - a
    b = c - b
    print('Переменная а равна: ', a)
    print('Переменная b равна: ', b)


def part_3():
    # Задача-3: Запросите у пользователя его возраст.
    # Если ему есть 18 лет, выведите: "Доступ разрешен",
    # иначе "Извините, пользование данным ресурсом только с 18 лет"
    age = inp_var("Укажите ваш возраст :", 0)
    if age >= 18:
        print ('Доступ разрешен')
    else:
        print('Доступ запрещен')

answer = 'Y'
while answer == 'Y' or answer == 'y':
    answer = part_hw_choose()
print("Вы закончили проверять мое домашнее задание, спасибо!")

