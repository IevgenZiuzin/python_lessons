# Створіть програму "Англо-французський словник". Збережіть слово англйською та його переклад на французьку.
# Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані.
# Використовуйте словник для збереження інформації.

mydict = {
    "earth": "la terre",
    "wind": "vent",
    "fire": "feu",
    "water": "l'eau",
    "man": "homme"
}


def menu():
    q = input("1. Add\n2. Remove\n3. Search\n4. Edit\n5. Show\n6. Quit\n")
    if q not in "12345":
        return
    else:
        return prompt(q)


def type_word():
    return input("Type your word here: ")


def prompt(q):
    if q == "1":
        add(type_word())
    elif q == "2":
        remove(type_word())
    elif q == "3":
        search(type_word())
    elif q == "4":
        edit(type_word())
    elif q == "5":
        show()
    else:
        return
    menu()


def add(w):
    translation = input("In French: ")
    mydict[w] = translation


def remove(w):
    if mydict.get(w):
        mydict.pop(w)


def search(w):
    if mydict.get(w):
        print(f"\n{w} - {mydict[w]}\n")


def edit(w):
    if mydict.get(w):
        add(w)


def show():
    eng = ["English", "", *list(mydict.keys())]
    fr = ["French", "", *list(mydict.values())]
    for i in range(len(eng)):
        print(eng[i].ljust(15), fr[i].ljust(15))
    print("")


print("\nWelcome to English French Dictionary 1.0\n")
while True:
    prompt(menu())
    break
