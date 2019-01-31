# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
import os

class Klass:
    def __init__(self, name_kl):
        self.name_kl = name_kl

    def add_klass(self, lessons :list):
        with open("klass.txt", 'r') as lst_lines:
           lines = []
           for line in lst_lines:
               lines.append(line[:-1])
           print(lines)
           point =0
           for i in lines:
               print(i)
               if self.name_kl in i:
                   print(i)
                   point = 1
           if point == 0:
               print("not")


"""
                  st_i = list(i.split(','))



                  #print(st_i)
               else:
                   str_tmp = "{}, ".format(self.name_kl)
                   for s in lessons:
                       str_tmp = str_tmp + "{} : ,".format(s)
                   lines.append(str_tmp[:-1])

"""
    #def klass_info(self, param):
     #   return "Klass info"+param

class Stud (Klass):
    def add_stud(self, name_stud, parents_stud):
        add_string = "{}, {}, {}".format(self.name_kl, name_stud, parents_stud)
        return add_string
    def stud_info(self, name_stud, param):
        return "{}, {}".format(name_stud, param)

class Teach (Klass):
    def add_teach(self, teach_name, lesson):
        add_string = "{}, {}, {}".format(self, lesson, teach_name)
        return add_string

klass_1 = Klass("8h")
klass_1.add_klass(["trud", "russkiy"])