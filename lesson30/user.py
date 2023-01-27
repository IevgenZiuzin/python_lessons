import json
import random
import string


class User(dict):
    counter = 0
    ids = []
    logins = []

    def __init__(self, a):
        super().__init__()
        if type(a) == dict:
            self.update(
                dict.fromkeys(('name', 'lastname', 'phone', 'login', 'password', 'id', 'results', 'saved')))
            self.update(a)
            if self.__class__.counter == 0:
                self.update(dict(isadmin=True))
            if self['login'] not in self.__class__.logins:
                self.__class__.logins.append(self['login'])
            if self['id'] and self['id'] not in self.__class__.ids:
                self.__class__.ids.append(self['id'])
            if not self['id']:
                self['id'] = self.create_id()
            self.__class__.counter += 1
        if type(a) == str and a not in self.__class__.logins:
            self.update(
                dict.fromkeys(('name', 'lastname', 'phone', 'login', 'password', 'id', 'results', 'saved')))
            if self.__class__.counter == 0:
                self.update(dict(isadmin=True))
            self['login'] = a
            self.__class__.logins.append(a)
            self.update({'id': self.create_id()})
            self.__class__.ids.append(self['id'])
            self.__class__.counter += 1

    def __str__(self):
        return self['id']

    @classmethod
    def create_id(cls):
        while True:
            n = "".join([str(random.choice(string.digits)) for i in range(4)])
            if n not in cls.ids:
                return str(n)

    @classmethod
    def check_login(cls, l):
        return False if l in cls.logins else True

    # @classmethod
    # def update_classdata(cls, c, i, l):
    #     cls.counter, cls.ids, cls.logins = c, i, l

    @classmethod
    def get_classdata(cls):
        return cls.counter, cls.ids, cls.logins

    def json(self):
        return json.dumps(self)

    def set_login(self, l):
        if self.check_login(l):
            self['login'] = l
            self.__class__.logins.append(l)
        else:
            return

    def set_password(self, p):
        self['password'] = p


def init(a):
    u = User(a)
    return u if u else False


def get_classdata():
    return User.get_classdata()