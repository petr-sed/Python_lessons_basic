# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

def make_dir(name, stat, path = os.getcwd()):
    list_dirs = os.listdir(path)
    if name in list_dirs:
        if stat is "stat_del":
            os.rmdir(name)
            print("Папка {} обнаружена и удалена".format (name))
        elif stat is "stat_write":
            print("Папка {} уже сущеcтвует".format(name))
    else:
        if stat is "stat_write":
            os.mkdir(name)
            print("Папка {} создана".format(name))
        elif stat is "stat_del":
            print("Папка {} не сущеcтвует".format(name))

path = os.getcwd()
list_dirs = os.listdir(path)

for i in range(1, 10):
    dir_nm = "dir_%s" % i
    if dir_nm in list_dirs:
        make_dir(dir_nm, "stat_del")
    else:
        make_dir(dir_nm, "stat_write")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
"""
print(list_dirs)
list_new = list(item for item in list_dirs if item.find('.') is -1)
print(list_new)
"""
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

"""
script_nm = os.path.basename(__file__)
script_nm = os.path.join(dir_path, script_nm)

script_copy = script_nm[0: script_nm.find('.')]+ '_copy.py'
content = ''
with open(script_nm, 'r', encoding='UTF-8') as f:
    content = f.readlines()
with open(script_copy, 'w', encoding='UTF-8')as f:
    for index in content:
        f.write(index + '\n')
"""



