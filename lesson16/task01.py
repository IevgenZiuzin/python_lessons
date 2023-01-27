# Есть четыре списка целых. Необходимо объединить в пятом списе только те элементы,
# которые уникальны для каждого списка. Полученный результат
# в зависимости от выбора пользователя отсортировать по убыванию или возрастаниюю
# Найти значение, введенное пользователем, с использованием бинарного поиска.
import random
import functools

inner_list_length = 4
outer_list_length = 4


def get_lists():
    return [[random.randint(1, 10) for i in range(inner_list_length)] for k in range(outer_list_length)]


def get_unics(l):
    sets = list(map(set, l))
    return l, sets, list(functools.reduce(lambda i, k: i ^ k, sets))


def display(l):
    print(f"lists: {get_unics(l)[0]}")
    print(f"sets:  {get_unics(l)[1]}")
    print(f"unics: {get_unics(l)[2]}")


def bin_search(l, n):
    first = 0
    last = len(l) - 1

    while first <= last:
        middle = (first + last) // 2
        if l[middle] < n:
            first = middle + 1
        elif l[middle] > n:
            last = middle - 1
        else:
            return middle
    return -1


def find():
    global lists
    while True:
        query = input("Type element to find or just Enter to return: ")
        unics_sorted = sorted(get_unics(lists)[2])
        try:
            print(f"Index of {query} in unics: [{bin_search(unics_sorted, int(query))}]")
        except:
            break


def get_sorted(n):
    global lists
    if n == "1":
        b = False
    elif n == "2":
        b = True
    else:
        return
    print(f"Ascending: {sorted(get_unics(lists)[2], reverse=b)}")


def menu():
    q = input("1. Sort ascending\n2. Sort descending\n3. Find element\n4. Regenerate\n5. Quit \n")
    if q not in "1234":
        return
    else:
        return prompt(q)


def prompt(q):
    global lists
    if q == "1":
        get_sorted(q)
    elif q == "2":
        get_sorted(q)
    elif q == "3":
        find()
    elif q == "4":
        lists = get_lists()
        display(lists)
    else:
        return
    menu()


lists = get_lists()
display(lists)
prompt(menu())

