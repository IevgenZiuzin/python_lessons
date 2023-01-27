"""
Дан текстовый файл. Необходимо создать новый файл
и записать в него следующую статистику по исходному файлу:
- количество символов;
- количество строк;
- количество гласных букв;
- количество согласных букв;
- количество цифр.
"""
import re


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


def write(n, t):
    file = open(n, "a")
    file.write(t)
    file.close()


def chars(t):
    return len(t)


def lines(f):
    return len(flines(f))


def vowels_consonants(t, f):
    if f == "v":
        l = "aeiou"
    elif f == "c":
        l = "bcdfghjklmnprstqvfxz"
    else:
        return
    return len(re.findall(f"{[l]}", t))


def digits(t):
    return len(re.findall("\d", t))


path_1, path_2 = ("text_1.txt", "text_2.txt")
text = ftext(path_1)
titles = ["Origin", "Chars", "Lines", "Vowels", "Consonants", "Digits"]
rows = [text, chars(text), lines(path_1),
        vowels_consonants(text, "v"),
        vowels_consonants(text, "c"),
        digits(text)]

for i, k in zip(titles, rows):
    print(f"{i}: {k}")
    if i != titles[0]:
        line = f"{i}: {k}\n"
        write(path_2, line)

