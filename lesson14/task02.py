# Написать программу "книги". Создать два списка с данными.
# Один список хранит названия книг, второй - годы выпуска.
# Реализовать меню для пользователя:
# - отсортировать по названию книг;
# - отсортировать по годам выпуска;
# - вывести список книг с названиями и годами выпуска;
# - выход.

import random
import string


def create_title():
    title = ""
    for i in range(random.randint(7, 12)):
        title += random.choice(string.ascii_lowercase)
    return title.title()


def get_sorted(*lists):
    return list(sorted(zip(*lists)))


def display(n):
    for i in n:
        print(str(i[0]).ljust(13), i[1])


def menu():
    q = input("1. Display start position\n2. Sort by years\n3. Sort by titles\n4. Quit\n")
    if q not in "123":
        return
    else:
        return prompt(q)


def prompt(q):
    if q == "1":
        display(zip(years, titles))
    elif q == "2":
        display(get_sorted(years, titles))
    elif q == "3":
        display(get_sorted(titles, years))
    else:
        return
    menu()


amount = 5
years = [str(random.randint(1971, 2022)) for i in range(amount)]
titles = [create_title() for i in range(amount)]


while True:
    prompt(menu())
    break

