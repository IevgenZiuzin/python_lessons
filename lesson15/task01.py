# Необходимо отсортировать первые две трети списка в порядке возрастания,
# если среднее арифметическое всех элементов больше нуля;
# иначе - лишь первую треть. Остальную часть списка не сортировать, а расположить в обратном порядке.

import random


def get_list():
    return [random.randint(-10, 10) for i in range(random.randint(0, 10))]


def get_sorted(l):
    if len(l) < 3:
        return l

    if sum(l)/len(l) > 0:
        i = 2 * len(l) // 3
    else:
        i = len(l) // 3

    l_sorted = sorted(l[:i])
    l_reversed = l[i:]
    l_reversed.reverse()
    print(f"\nOriginal: {l}\nSorted:   {l_sorted + l_reversed}\n")


def run():
    while True:
        get_sorted(get_list())
        query = input("Type \"y\" for repeat, any key for exit: ")
        if query != "y":
            break


run()
