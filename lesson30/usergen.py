import random
import string

default_names = ["danny", "eli", "terry", "shay", "alex", "reggie", "jordan", "billy", "maddox", "ryan"]
default_lastnames = ["armstrong", "rees", "elliot", "brooks", "cooper",
                    "vincent", "fisher" "perry", "singleton", "harrell"]
default_codes = ["067", "068", "096", "097", "098", "050", "066", "095", "099", "063", "073", "093"]
default_agerange = (20, 60)


class Usergen:
    id_s = []
    logins = []

    def __init__(self, names=None, lastnames=None, agerange=None, codes=None):
        self.names = names or default_names
        self.lastnames = lastnames or default_lastnames
        self.agerange = agerange or default_agerange
        self.codes = codes or default_codes

    def id(self):
        while True:
            n = "".join([str(random.choice(string.digits)) for i in range(4)])
            if n not in self.__class__.id_s:
                return str(n)

    def login(self):
        while True:
            n = self.name().title() + self.lastname().title()
            if n not in self.logins:
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


def init():
    pass