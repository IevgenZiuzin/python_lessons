"""
Напишите информационную систему «Сотрудники».Программа должна обеспечивать
ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск сотрудника по фамилии,
вывод информации обо всех сотрудниках указанного возраста,
или фамилия которых начинается на указанную букву.
Организуйте возможность сохранения найденной информации в файл. Также весь
список сотрудников сохраняется в файл (при выходе из программы — автоматически, в процессе исполнения
программы — по команде пользователя). При старте программы происходит загрузка списка сотрудников из
указанного пользователем файла.
"""
import json
import numbmenu
import staff


def load(p):
    file = open(p)
    text = file.read()
    file.close()
    try:
        d = json.loads(text)
        e = staff.Employees(list(d.keys()))
        for i, k in d.items():
            e[i] = staff.Employee(i)
            e[i].update_user(k)
        return e
    except ValueError:
        return staff.Employees([], path)


def generate_staff(n):
    gen = staff.Usergen()
    id_s = [gen.id() for i in range(n)]
    e = staff.Employees(id_s)
    for i in id_s:
        e[i] = staff.Employee(i)
        e[i].update_user({"name": gen.name(), "lastname": gen.lastname(),
                     "age": gen.age(), "phone": gen.phone()})
    return e


path = "staff.txt"
firm = load(path)
# firm = generate_staff(10)


menu_items = ("Add", "Edit", "Remove", "Save", "Show all",
              "Search by ID", "Search by value", "Search by match")
commands = (firm.add, firm.edit, firm.remove, firm.save, firm.show_all,
            firm.search_id, firm.search_value, firm.search_match)

menu = numbmenu.init(menu_items, commands)

print("\nWelcome to YourStuff 2.0\n")
menu.run()
firm.save()
print("See you!")
