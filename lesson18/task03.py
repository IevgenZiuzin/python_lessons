# Есть кортеж с названиями производителей автомобилей (название производителя может встречаться от 0 до N раз).
# Пользователь вводит с клавиатуры название производителя и слово для замены.
# Необходимо заменить в кортеже все элементы с этим названием на слово для  замены.
# Совпадение по названию должно быть полным.
import random

brands_list = ["Toyota", "Honda", "Chevrolet", "Ford", "Mercedes-Benz", "Jeep", "BMW", "Porsche", "Subaru",
               "Nissan"]


def run():
    brands_tuple = tuple(random.choice(brands_list) for i in range(10))
    print(brands_tuple)

    query = input("to replace: ")

    if query in brands_tuple:
        replacer = input("replace with: ")
        temp = list(brands_tuple)
        for i in range(len(temp)):
            if temp[i] == query:
                temp[i] = replacer

        brands_tuple = tuple(temp)
        print(brands_tuple)
    else:
        print(f"no matches for \"{query}\"")


while True:
    run()
    prompt = input("repeat y/n: ")
    if prompt != "y":
        break
