# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random
old_list = [random.randint(-30,30) for _ in range(20)]
print(old_list)
new_list = list(map(lambda x: x*x, old_list))
print(new_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list_1 = ["яблоко", "апельсин", "мандарин", "лимон"]
list_2 = ["мандарин", "яблоко", "слива", "груша"]

new_list = []
for i in range(len(list_1)):
    if list_1[i] in list_2:
        new_list.append(list_1[i])
print(new_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
new_list=[]
for i in range (len(old_list)):
    if old_list[i] > 0 and old_list[i]%3 is 0 and old_list[i]%4 > 0:
        new_list.append(old_list[i])
print(new_list)