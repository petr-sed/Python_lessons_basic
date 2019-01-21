# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import os
"""
stroka = []
stroka_2 = []
summa = 0
#открываю файл "workers" построчно присваиваю значения переменной в виде массива
with open(os.path.join('data', 'workers'), "r", encoding = "utf=8") as file:
    for line in file:
        stroka = line.split()
        #открываю второй файл и построчно ищу нужную строку по соостветствию имени и фамилии
        with open(os.path.join('data', 'hours_of'), "r", encoding = "utf=8") as scnd_file:
            for line_1 in scnd_file:
                stroka_2 = line_1.split()
                #найдя строку имя и фамилия в которой совпадают с искомыми вытаскиваю значение отработанных часов
                if stroka[0] == stroka_2[0] and stroka[1] == stroka_2[1] and stroka[0] != 'Имя':
                   summa = summa + (int(stroka_2[2])/int(stroka[4]))*int(stroka[2])
print(int(round(summa, 0)))
"""



# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
"""
with open(os.path.join('data', 'fruits.txt'), "r", encoding="utf-8") as file:
    for line in file:
        fr = str(line)
        if fr != '\n':
            lit = fr[0]
            fl_name = 'fruits_%s%s' %(lit, '.txt')
            #print(fl_name)
            with open(os.path.join('data', fl_name), "a", encoding="utf-8") as file:
               file.write(fr)
"""

