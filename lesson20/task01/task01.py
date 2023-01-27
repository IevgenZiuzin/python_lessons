"""
Дано два текстовых файла. Выяснить, совпадают ли их строки.
Если нет, то вывести несовадающую строку из каждого файла.
"""
import functools


def ftext(f):
    file = open(f)
    text = file.read()
    file.close()
    return text


def flines(f):
    file = open(f)
    lines = list(map(lambda i: i.strip(), file.readlines()))
    file.close()
    return lines


def get_unics(l):
    sets = list(map(set, l))
    return functools.reduce(lambda i, k: i ^ k, sets)


path_1, path_2 = ("text_1.txt", "text_2.txt")
line_lists = [flines(path_1), flines(path_2)]
unics = get_unics(line_lists)

print(f"text_1.txt:\n{ftext(path_1)}\n")
print(f"text_2.txt:\n{ftext(path_2)}\n")
print("Unics:")
for i in unics:
    print(i)
