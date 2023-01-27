# Створіть програму "Фірма", яка зберігає інформацію про працівників:
# ПІБ, телефон, корпоративний email, назва посади, номер кабінету, Skype.
# Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані.
# Використовуйте словник для збереження інформації.

#

import random

id_s = []
employees = dict()
employee = dict(surname="", firstname="", fathername="", phone="", jobtitle="", room="", skype="")


def create_id():
    while True:
        n = str(random.randint(10, 99))
        if n not in id_s:
            id_s.append(n)
            return n


def get_id():
    return input("Type user ID: ")


def add():
    user_id = create_id()
    employees[user_id] = employee.copy()
    print(f"adding user ID \"{user_id}\"")
    for i in employee.keys():
        employees[user_id][i] = input(f"{i}: ")


def edit(n):
    if employees.get(n):
        print(f"field names: {', '.join(list(employees[n].keys()))}")
        while True:
            query = input("\nType field name to edit it, \"a\" to change all, \"s\" to stop editing: ")
            if query in list(employees[n].keys()):
                print(f"current: {employees[n][query]}")
                employees[n][query] = input("new: ")
            elif query == "a":
                for k in employees[n].keys():
                    print(f"current {k}: {employees[n][k]}")
                    employees[n][k] = input(f"new: ")
            else:
                break
    else:
        print(f"\nno user with ID: \"{n}\"\n")


def remove(n):
    if employees.get(n):
        employees.pop(n)
        i = id_s.index(n)
        id_s.pop(i)
        print(f"\nid \"{n}\" removed\n")
    else:
        print(f"\nno user with ID: \"{n}\"\n")


def search(n):
    if employees.get(n):
        for i in employees[n].keys():
            print(str(i).ljust(10), str(employees[n][i]).ljust(10))
        print("")
    else:
        print(f"\nno user with ID: \"{n}\"\n")


def show_all():
    keys = [*employees.keys()]
    for i in keys:
        print(f"\nID \"{i}\":")
        for k in employees[i].keys():
            print(str(k).ljust(10), str(employees[i][k]).ljust(10))
        print("")


def show_ids():
    print(id_s)


def menu():
    q = input("1. Add\n2. Remove\n3. Search by ID\n4. Edit\n5. Show all\n6. Show ID's\n7. Quit\n")
    if q not in [n for n in "123456"]:
        return
    else:
        return prompt(q)


def prompt(q):
    if q == "1":
        add()
    elif q == "2":
        remove(get_id())
    elif q == "3":
        search(get_id())
    elif q == "4":
        edit(get_id())
    elif q == "5":
        show_all()
    elif q == "6":
        show_ids()
    else:
        return
    menu()


print("\nWelcome to YourStuff 1.0\n")
while True:
    prompt(menu())
    break
