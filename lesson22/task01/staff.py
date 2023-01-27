import json
import random
import string
import re

default_names = ["danny", "eli", "terry", "shay", "alex", "reggie", "jordan", "billy", "maddox", "ryan"]
default_lastnames = ["armstrong", "rees", "elliot", "brooks", "cooper", "vincent", "fisher" "perry", "singleton", "harrell"]
default_codes = ["067", "068", "096", "097", "098", "050", "066", "095", "099", "063", "073", "093"]
default_agerange = (20, 60)


def write(n, t, f):
    file = open(n, f)
    file.write(t)
    file.close()


def display_emp(d):
    for i in d.keys():
        print(f"\nID \"{i}\":")
        for k in d[i].keys():
            print(str(k).ljust(10), str(d[i][k]).ljust(10))
        print("")
        print(f"Results: {len(d)}")


def save_results(d):
    if len(d) > 0:
        display_emp(d)
        query = input("Do you want to save search results? (y/n): ")
        if query != "y":
            return
        else:
            path = input("Type filename for saving: ") + ".txt"
            write(path, json.dumps(d), "w")
            print(f"{path} saved")
    else:
        print("Nothing found")


class Employee(dict):
    def __init__(self, id=None):
        super().__init__(name="", lastname="", age="", phone="")
        self.id = id or ""

    def __str__(self):
        return self.id


class Employees(dict):
    def __init__(self, id_s=None, path=None):
        super().__init__()
        self.ids = id_s or []
        self.path = path or "staff.txt"

    def create_id(self):
        while True:
            n = str(random.randint(1001, 9999))
            if n not in self.ids:
                self.ids.append(n)
                return str(n)

    def add(self):
        user_id = self.create_id()
        self[user_id] = Employee()
        print(f"adding user ID \"{user_id}\"")
        for i in self[user_id].keys():
            self[user_id][i] = input(f"{i}: ")

    def edit(self):
        e = input("Type ID: ")
        if self.get(e):
            print(f"field names: {', '.join(list(self[e].keys()))}")
            while True:
                query = input("\nType field name to edit it, \"a\" to change all, \"s\" to stop editing: ")
                if query in list(self[e].keys()):
                    print(f"current: {self[e][query]}")
                    self[e][query] = input("new: ")
                elif query == "a":
                    for k in self[e].keys():
                        print(f"current {k}: {self[e][k]}")
                        self[e][k] = input(f"new: ")
                else:
                    break
        else:
            print(f"\nno user with ID: \"{n}\"\n")

    def remove(self):
        e = input("Type ID: ")
        if self.get(e):
            self.pop(e)
            i = self.ids.index(e)
            self.ids.pop(i)
            print(f"\nid \"{e}\" removed\n")
        else:
            print(f"\nno user with ID: \"{e}\"\n")

    def save(self):
        write(self.path, json.dumps(self), "w")
        print("Saved")

    def show_all(self):
        display_emp(self)

    def search_id(self):
        q = input("Type ID: ")
        if q in self.keys():
            display_emp({q: self[q]})
        else:
            print(f"ID {q} not found")

    def search_value(self):
        result_dict = dict()
        q = input("Type any value to find employee of it: ").lower()
        for i in self.keys():
            if q in list(map(lambda x: x.lower(), self[i].values())):
                result_dict[i] = self[i]
        save_results(result_dict)

    def search_match(self):
        result_dict = dict()
        q = input("Type any beginning of value to find employee of it: ").lower()
        for i in self.keys():
            for k in self[i].values():
                if re.search(f"^{q}", k.lower()):
                    result_dict[i] = self[i]
        save_results(result_dict)


class Usergen:
    def __init__(self, id_s=None, names=None, lastnames=None, agerange=None, codes=None):
        self.id_s = id_s or []
        self.names = names or default_names
        self.lastnames = lastnames or default_lastnames
        self.agerange = agerange or default_agerange
        self.codes = codes or default_codes

    def id(self):
        while True:
            n = str(random.randint(1001, 9999))
            if n not in self.id_s:
                self.id_s.append(n)
                return str(n)

    def name(self):
        name = random.choice(self.names)
        return name.title()

    def lastname(self):
        lastname = random.choice(self.lastnames)
        return lastname.title()

    def age(self):
        return str(random.randint(self.agerange[0], self.agerange[1]))

    def phone(self):
        number = random.choice(self.codes)
        for i in range(7):
            number += random.choice(string.digits)
        return number



