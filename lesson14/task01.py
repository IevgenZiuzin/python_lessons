# Написать программу "справочник". Создать два списка целых.
# Один список хранит идентификационные коды, второй - телефонные номера.
# Реализовать меню для пользователя:
# - отсортировать по идентификационным кодам;
# - отсортировать по номерам телефона;
# - вывести список пользователей с кодами и телефонами;
# - выход.

import random
import string


def create_code():
    code = ""
    for i in range(10):
        code += random.choice(string.digits)
    return code


def create_number():
    number = random.choice(["067", "068", "096", "097", "098", "050", "066", "095", "099", "063", "073", "093"])
    for i in range(7):
        number += random.choice(string.digits)
    return number


def get_sorted(*lists):
    return list(sorted(zip(*lists)))


def display(n):
    for i in n:
        print(str(i[0]).ljust(13), i[1])


def menu():
    q = input("1. Display start position\n2. Sort by codes\n3. Sort by numbers\n4. Quit\n")
    if q not in "123":
        return
    else:
        return prompt(q)


def prompt(q):
    if q == "1":
        display(zip(numbers, codes))
    elif q == "2":
        display(get_sorted(codes, numbers))
    elif q == "3":
        display(get_sorted(numbers, codes))
    else:
        return
    menu()


amount = 5
numbers = [create_number() for i in range(amount)]
codes = [create_code() for i in range(amount)]


while True:
    prompt(menu())
    break
