print("""Пользователь с клавиатуры вводит элементы списка целых.
Необходимо посчитать сумму всех элементов и их среднеарифметическое.
Результаты вывести на экран.""")

integers = []

while True:
    integer = input("Add integer to list (\"\" or not integer for stop): ")
    try:
        integers.append(int(integer))
    except:
        break
if len(integers) > 0:
    print(f"Sum: {sum(integers)}\nAverage: {sum(integers)/len(integers)}")
else:
    print("This list is empty", integers)
