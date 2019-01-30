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

class student:
    def __init__(self, name):
        self.name = name

    def add_student(self, klass, parents):
        with open("students.txt", 'a') as file_stud:
            file_stud.write("{}; {}; {}\n".format(self.name, klass, parents))
        list_klasses = []
        klass = klass+'_students'
        with open("klass.txt", 'r') as file_klass:
           for line in file_klass:
               list_klasses.append(line[:-1])
        if klass in list_klasses:
            ind = list_klasses.index(klass)
            list_klasses.insert(ind+1, self.name)
            str_klasses = ''
            for i in list_klasses:
                str_klasses = str_klasses + i + '\n'
            with open("klass.txt", 'w') as file_klass:
                file_klass.write(str_klasses)
        else:
            with open("klass.txt", 'a') as file_klass:
                file_klass.write("{}\n{}\n".format(klass, self.name))





    def add_teacher(self, klass, lesson):
        with open("teachers.txt", 'a') as file_stud:
             file_stud.write("{}; {}; {}\n".format(self.name, klass, lesson))
        list_klasses = []
        klass = klass + '_lessons'
        with open("klass.txt", 'r') as file_klass:
            for line in file_klass:
                list_klasses.append(line[:-1])
        if klass in list_klasses:
            ind = list_klasses.index(klass)
            list_klasses.insert(ind + 1, "{} : {}".format(lesson, self.name))
            str_klasses = ''
            for i in list_klasses:
                str_klasses = str_klasses + i + '\n'
            with open("klass.txt", 'w') as file_klass:
                file_klass.write(str_klasses)
        else:
            with open("klass.txt", 'a') as file_klass:
                file_klass.write("{}\n{} : {}\n".format(klass, lesson, self.name))

teacher_1 = student("Teacher1 A.B.")
teacher_1.add_teacher("5c", "algebra")

