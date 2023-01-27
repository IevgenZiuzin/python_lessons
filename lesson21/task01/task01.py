"""
Пользователь с клавиатуры вводит названия файлов, до тех пор,
пока он не введет слово quit. После завершения ввода программа должна
записать в итоговый файл символы, которые есть во всех перечисленных файлах
(символы должны быть в каждом файле).
"""


import functools
import random

inner_list_length = 4
outer_list_length = 4
paths = []
current_paths = ["a.txt", "b.txt", "c.txt", "d.txt"]
result_file = "result.txt"


def ftext(f):
    file = open(f)
    text = file.read()
    file.close()
    return text


def write(n, t, f):
    file = open(n, f)
    file.write(t)
    file.close()


def get_commons(l):
    sets = list(map(set, l))
    return list(functools.reduce(lambda i, k: i & k, sets))


def get_lists():
    return [[random.randint(1, 10) for i in range(inner_list_length)] for k in range(outer_list_length)]


def input_paths():
    global paths, current_paths
    while True:
        path = input("Type file.py name without extension: ")
        if path == "quit":
            break
        name = path + ".txt"
        if name in current_paths:
            paths.append(name)


def generate():
    random_chars = get_lists()
    for index, path in enumerate(current_paths):
            inner_list = random_chars[index]
            line = ", ".join([str(i) for i in inner_list])
            write(path, line, "w")


def write_unics():
    global paths
    lines = []
    for i in paths:
        lines.append([k for k in ftext(i)])
    commons = sorted((get_commons(lines)))
    print(commons)
    commons = ["\"" + i + "\"" for i in commons]
    write(result_file, "Common characters: ", "w")
    write(result_file, ", ".join(commons), "a")


generate()
input_paths()
write_unics()
for i in current_paths:
    print(ftext(i))






