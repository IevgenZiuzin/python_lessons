"""
Дан текстовый файл. Удалить из него последнюю строку. Результат записать в другой файл.
"""


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


def write(n, t, f):
    file = open(n, f)
    file.write(t)
    file.close()


path_1, path_2 = ("text_1.txt", "text_2.txt")
text = ftext(path_1)
rows = flines(path_1)
print(f"Origin: ")
for i in rows:
    print(i)
print("Edited:")
for i in rows[:len(rows)-1]:
    print(i)
    write(path_2, i + "\n", "a")



