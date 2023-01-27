# Реализовать программу расчета заказа в кафетерии при условии, что заказ может
# быть на несколько человек и каждый клиент формирует свою часть заказа.
# Необходимо спросить у пользователя на сколько человек заказ. Далее каждому
# человеку выводиться меню (названия напитков, кондитерских изделий и их цена) и он
# выбирает. Предусмотреть возможность выбора нескольких элементов меню для
# клиента, если он желает добавить еще что-то в свой заказ. Результат работы
# программы — итоговая сумма общего заказа всей компании

foods = [{"Coffee": 1.25},
         {"Cola": 0.9},
         {"Beer": 1.5},
         {"Icecream": 1.3},
         {"Burger": 2},
         {"Cake": 2.1},
         ]


def get_name_price(n):
    index = int(n) - 1
    name = list(foods[index].keys())[0]
    price = list(foods[index].values())[0]
    return [name, price]


def get_menu(menu):
    menu_string = ""
    if len(menu) > 0:
        for i in range(len(menu)):
            name = list(menu[i].keys())[0]
            price = list(menu[i].values())[0]
            menu_string += "{0} - {1:10} - ${2}\n".format((i + 1), name, price)
    return menu_string


current_menu = get_menu(foods)

try:
    total_order = []
    guest_order = []
    orders = 0

    guests = int(input("How many of you: "))

    for i in range(1, guests + 1):

        guest_order_prices = []
        guest_order_names = []

        while True:
            print(f"\nGuest {i}:\n{current_menu}")
            order_query = input(f"(number and 'enter' for choice, just 'enter' to skip and go next)\nYour choice: ")
            if order_query == "":
                break

            name = get_name_price(order_query)[0]
            price = get_name_price(order_query)[1]

            guest_order_prices.append(price)
            guest_order_names.append(name)

            print(f"\nGuest {i} selection: {', '.join(guest_order_names)}\nSum: ${sum(guest_order_prices)} \n\n")

        if len(guest_order_names) > 0:

            total_order.append(sum(guest_order_prices))
            guest_order.append(guest_order_names)

            orders += 1

        else:
            continue

    print(f"\n\nGuests: {guests}")

    for i in range(orders):
        print(f"Order {i + 1}: ${total_order[i]} ({', '.join(guest_order[i])})")

    print(f"Total: ${sum(total_order)}")

except:
    print("wrong value")
