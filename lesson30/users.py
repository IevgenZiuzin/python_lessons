import json
import re
import user


class Users(dict):
    path = 'users.txt'

    def __init__(self):
        super().__init__()

    @staticmethod
    def write(n, t, f):
        file = open(n, f)
        file.write(t)
        file.close()

    @staticmethod
    def save_results(d):
        if len(d) > 0:
            Users.display_user(d)
            query = input("Do you want to save search results? (y/n): ")
            if query != "y":
                return
            else:
                path = input("Type filename for saving: ") + ".txt"
                Users.write(path, json.dumps(d), "w")
                print(f"{path} saved")
        else:
            print("Nothing found")

    @staticmethod
    def display_user(d):
        for i in d:
            print(f"\nID \"{i}\":")
            for k in d[i]:
                print(str(k).ljust(10), str(d[i][k]).ljust(10))
            print("")
            print(f"Results: {len(d)}")

    def add(self):
        d = dict.fromkeys(('password', 'name', 'lastname', 'phone'))
        q = input('set login: ')
        if q == '':
            return
        u = user.init(q)
        print(f"adding user ID \"{u}\"")
        for i in d:
            d[i] = input(f"set {i}: ")
        u.update_user(d)
        self.update({str(u): u})
        self.save()

    def edit(self):
        q = input("Type ID: ")
        if self.get(q):
            d = dict.fromkeys(('name', 'lastname', 'phone'))
            print(f"field names: {', '.join(list(d.keys()))}")
            while True:
                query = input("\nType field name to edit it, \"a\" to change all, \"s\" to stop editing: ")
                if d.get(query):
                    print(f"current: {self[q][query]}")
                    d[query] = input("new: ")
                elif query == "a":
                    for k in d:
                        print(f"current {k}: {self[q][k]}")
                        d[k] = input(f"new: ")
                else:
                    break
            self[q].update_user(d)
            self.save()
        else:
            print(f"ID {q} not found")

    def remove(self):
        q = input("Type ID: ")
        if self.get(q):
            del self[q]
            print(f"\nid \"{q}\" removed\n")
        else:
            print(f"ID {q} not found")

    def save(self):
        self.__class__.write(self.__class__.path, json.dumps(self), "w")
        print("Saved")

    def show_all(self):
        self.__class__.display_user(self)

    def search_id(self):
        q = input("Type ID: ")
        if self.get(q):
            self.__class__.display_user({q: self[q]})
        else:
            print(f"ID {q} not found")

    # def search_value(self):
    #     d = dict()
    #     q = input("Type any value to find user of it: ").lower()
    #     for i in self:
    #         if q in list(map(lambda x: str(x).lower(), self[i].values())):
    #             d[i] = self[i]
    #     self.__class__.save_results(d)

    def search_match(self):
        d = dict()
        q = input("Type any beginning of value to find user of it: ").lower()
        for i in self:
            for k in self[i].values():
                if re.search(f"^{q}", str(k).lower()):
                    d[i] = self[i]
        self.__class__.save_results(d)


def init():
    return Users()
