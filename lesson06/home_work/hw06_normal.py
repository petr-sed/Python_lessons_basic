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
        lessons = str(lessons)
        return "Klass added: "+lessons

    def klass_info(self, param):
        return "Klass info"+param

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
