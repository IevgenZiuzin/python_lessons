import user
import users
import usergen
import json


# t1 = task.init('how are you', ['asdf', 'zxcv', 'qwer'], ['asdf', 'qwer'])
# t2 = task.init('how is he', ['asdf', 'zxcv', 'qwer'], 'zxcv')
# t3 = task.init('how is she', ['asdf', 'zxcv', 'qwer'], 'qwer')
# t4 = task.init('how are they', ['asdf', 'zxcv', 'qwer'], 'asdf')
# t5 = task.init('how are we', ['asdf', 'zxcv', 'qwer'], 'asdf')
# t6 = task.init('how am i', ['asdf', 'zxcv', 'qwer'], 'zxcv')


# print(t1)
# tests_list = [t1, t2, t3, t4, t5, t6]
# test = test.init("some name", tests_list)
# print(test)
# t7 = task.init('what time is it', [1, 2, 3], 2)
# tests_list.append(t7)
# print(test)


def write(n, t, f):
    file = open(n, f)
    file.write(t)
    file.close()


def read(f):
    file = open(f)
    text = file.read()
    file.close()
    return text


def generate_staff(n):
    gen = usergen.Usergen()
    us = users.init()
    for i in range(n):
        n = gen.login()
        u = user.init(n)
        us[u['id']] = u
    return us


def save(o):
    write('users.txt', json.dumps(o), "w")
    return o


# save(generate_staff(5))


# loaded = json.loads(ftext('users.txt'))
# print(f'loaded {loaded}')
# returned = dict()
# for i in loaded.keys():
#     u = user.init(loaded[i])
#     returned.update({u['id']: u})
# print(returned)

