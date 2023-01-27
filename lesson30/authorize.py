import json
import numbmenu
import user
import users
import adminmod
import usermod
import tests
import test


class Authorize:

    @staticmethod
    def read(f='users.txt'):
        file = open(f)
        text = file.read()
        file.close()
        return text

    @staticmethod
    def write(b, f, n='users.txt'):
        file = open(n, f)
        file.write(json.dumps(b))
        file.close()

    @staticmethod
    def load_users():
        us = users.init()
        s = json.loads(Authorize.read())
        for i in s:
            u = user.init(s[i])
            us.update_user({u['id']: u})
        return us

    @staticmethod
    def load_tests():
        tsts = tests.init()
        return tsts

    @staticmethod
    def check_login(login, p='users.txt'):
        o = json.loads(Authorize.read(p))
        for i in o:
            if o[i].get('login') == login:
                return o[i]
        return False

    @staticmethod
    def check_pass(l, p):
        u = Authorize.check_login(l)
        if u and u.get('password') == p:
            return u
        return False

    @staticmethod
    def isadmin(u):
        return u.get('isadmin')

    @staticmethod
    def switch(u):
        if Authorize.isadmin(u):
            print('admin mod')
            adm = adminmod.init()
            admin_menu = numbmenu.init(['Users', 'Stats', 'Tests'], [adm.users_mod, adm.stats_mod, adm.tests_mod])
            admin_menu.run()
        else:
            print('user mod')
            usr = usermod.init()
            user_menu = numbmenu.init(['Test', 'Results'], [usr.tests_mod, usr.results_mod])
            user_menu.run()

    @staticmethod
    def sign_in():
        l = input('Login: ')
        p = input('Pass: ')
        u = Authorize.check_pass(l, p)
        if u:
            Authorize.switch(u)
        else:
            print('Wrong login or password.')

    @staticmethod
    def sign_up():
        userdata = Authorize.load_users()
        login = input('Login: ')
        if not Authorize.check_login(login):
            password = input('Pass: ')
            name = input('Name: ')
            lastname = input('Lastname: ')
            phone = input('Phone: ')
            u = user.init({'login': login, 'password': password, 'name': name, 'lastname': lastname, 'phone': phone})
            userdata.update_user({u['id']: u})
            Authorize.write(userdata, 'w')
            Authorize.switch(u)
        else:
            print('This login is already used.')


def init():
    return Authorize()
