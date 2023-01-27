import random
import requests


def create_id():
    while True:
        n = str(random.randint(10, 99))
        if n not in id_s:
            id_s.append(n)
            return n


response = requests.get("https://randomuser.me/api/?results=25")
id_s = []
users = []
randoms = response.json()['results']


def create_id():
    while True:
        n = str(random.randint(101, 999))
        if n not in id_s:
            id_s.append(n)
            return n


for i in randoms:
    name = i['name']
    i['id']['value'] = idn = create_id()
    full_name = idn.ljust(6) + name['title'].ljust(15) + name['first'].ljust(20) + name['last'].ljust(20)
    users.append(full_name)


print("ID".ljust(6) + "Title".ljust(15) + "First".ljust(20) + "Last".ljust(20))
users_dict = {}
for i, k in enumerate(users):
    print(k)
    users_dict.update({id_s[i]: randoms[i]})

query = input("Enter id: ")
if users_dict[query]:
    u = users_dict[query]
    print(f"ID: {u['id']['value']}\nStreet: {u['location']['street']['name']}\nCity: {u['location']['city']}\nState: {u['location']['state']}\nCountry: {u['location']['country']}\nEmail: {u['email']}\nLogin: {u['login']['username']}\nPassword: {u['login']['password']}")
else:
    print("no user found")


# Доробити програму - добавити можливість просмотру даних аккаунта по id*
# Користувач вводить id аккаунта та повинен побачити street, city, state, country, email, login, password
