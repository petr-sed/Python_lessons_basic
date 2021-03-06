# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

catalog = ["яблоко", "банан", "киви", "арбуз"]
print("Вывод:")
for i in range(len(catalog)):
    print('{number}. {fruit:>8}'.format(number = i+1, fruit = catalog[i]))



# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list_1 = [1, 2, 6, 9, 8, 9, 2, 4, 0]
list_2 = [9, 6, 7, 2, 21]
print(list_1)
print(list_2)
for i in range(len(list_2)):
    for a in range(list_1.count(list_2[i])):
        list_1.pop(list_1.index(list_2[i]))
print(list_1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
import math
list_1 = [1, 2, 6, 8, 16, 7, 3, 51]
list_2 = []
i = 0
while i < len(list_1):
    if list_1[i] % 2 == 0:
        list_2.append(int(list_1[i])/4)
    else:
        list_2.append(int(list_1[i])*2)
    i += 1
print(list_1)
print(list_2)