# Два списка целых заполняются случайными числами.
# Необходимо:
# ■ Сформировать третий список, содержащий элементы
# обоих списков;
# ■ Сформировать третий список, содержащий элементы
# обоих списков без повторений;
# ■ Сформировать третий список, содержащий элементы
# общие для двух списков;
# ■ Сформировать третий список, содержащий только
# уникальные элементы каждого из списков;
# ■ Сформировать третий список, содержащий только
# минимальное и максимальное значение каждого из
# списков.

import random as r

randoms = [[r.randint(-10, 10) for i in range(4)] for k in range(4)]

all_as_one = []
repeatings_excluded = []
commons_only = list(set.intersection(*map(set, randoms)))
unics_foreach = []
min_max_foreach = []
counter = 1;
for i in randoms:
    i.sort()
    all_as_one += i
    print(f"Random {counter}:{i}")
    unics = []
    for k in i:
        if k not in repeatings_excluded:
            repeatings_excluded.append(k)
        if k not in unics:
            unics.append(k)
    unics_foreach.extend(unics)
    min_max_foreach.append([min(i), max(i)])
    counter += 1

print(f"\n1. All as one:\n{all_as_one}")
print(f"\n2. All as one repeating excluded:\n{repeatings_excluded}")
print(f"\n3. All commons only as one:\n{commons_only}")
print(f"\n4. Unics for each as one:\n{unics_foreach}")
print(f"\n5. Mins and maxs for each:\n{min_max_foreach}")


