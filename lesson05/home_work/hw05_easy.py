# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

dir_path = os.getcwd()
list_dirs = os.listdir(dir_path)

for i in range(1, 10):
    dir_nm = "dir_%s" % i
    if dir_nm in list_dirs:
        os.rmdir(dir_nm)
    else:
        os.mkdir("dir_%s" % i)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print(list_dirs)
list_new = list(item for item in list_dirs if item.find('.') is -1)
print(list_new)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

