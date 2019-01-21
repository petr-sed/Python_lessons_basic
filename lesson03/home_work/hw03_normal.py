# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
def fibonacci(n, m):
    list_fib = []
    for i in range(m+1):
        if i<3:
            list_fib.append(1)
        else:
            list_fib.append(list_fib[i-1]+list_fib[i-2])
    return(list_fib[n:])

print(fibonacci(5,9))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
def sort_to_max(origin_list):
    new_list = []
    for i in range(len(origin_list)):
        new_list.append(origin_list.pop(origin_list.index(min(origin_list))))
    return(new_list)

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
list_old = ['сорняк', 'зерно', 'сорняк', 'зерно', 'сорняк', 'сорняк', 'зерно']

def my_filter(list_for_filter, name):
    list_filter = list_for_filter.count(name)
    list_new = []
    for i in range(list_filter):
        list_new.append(name)
    return(list_new)

print(my_filter(list_old, 'зерно'))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

#Принимаю координаты точек в виде четырех массивов, первой точкой считается верхняя левая
#Ввод строго по-порядку
first_point = [3, 7]
second_point = [10, 7]
third_point = [10, 2]
fourth_point = [3, 2]
# Исхожу из того, что у параллелограмма x1 = x4, x2 = x3, y1 = y2, y3 = y4
def paral_valid(frst_point, scnd_point, thrd_point, frth_point):
    # для сокращения длинны условия в if ввожу дополительныю переменную
    valid = (frst_point[0]-frth_point[0])+(scnd_point[0]-thrd_point[0])
    valid = valid + (frst_point[1]-scnd_point[1])+(thrd_point[1]-frth_point[1])
    if valid == 0:
        return("Фигура, образованная указанными точками, является пераллелограммом.")
    else:
        return ("Фигура, образованная указанными точками, не является пераллелограммом.")

print(paral_valid(first_point, second_point, third_point, fourth_point ))





