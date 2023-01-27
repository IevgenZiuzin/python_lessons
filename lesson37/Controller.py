# Створіть клас "Взуття", який має зберігати таку інформацію:
# - тип взуття:
# а) чоловіче
# б) жіноче
# - вид взуття (кросівки, чоботи, сандалі, туфлі тощо):
# - колір
# - ціна
# - виробник
# - розмір
# Створіть необхідні методи для цього класу. Реалізуйте
# MVC-патерн для класу "Взуття" та код для використання моделі,
# контролера та представлення.


import re
import menu
import random
import string
from Model import ProductsDB, ShoesBuilder1
from View import *


class DBEditor(list):
    def __init__(self, db=None):
        super().__init__()
        if db is not None:
            self.extend(db)
        self.codes = self.__codes()

    def __codes(self):
        return [product['code'] for product in self]

    def __create_code(self):
        while True:
            combination = ''.join([random.choice(string.digits) for _ in range(4)])
            if combination not in self.codes:
                self.codes.append(combination)
                return combination

    def __display(self):
        display_products(self)

    def __add(self):
        builder = ShoesBuilder1()
        builder.set_name(input('Name: '))
        if builder.product.name == '':
            return
        builder.set_gender(input('Gender: '))
        builder.set_form(input('Form: '))
        builder.set_color(input('Color: '))
        builder.set_vendor(input('Vendor: '))
        price, size = input('Price: '), input('Size: ')
        try:
            builder.set_price(float(price))
            builder.set_size(float(size))
        except ValueError:
            print('Float values incorrect format.')
        builder.set_code(self.__create_code())
        self.append(builder.product.__dict__)

    def __delete(self):
        query = input("Type product code to delete: ").lower()
        for index, product in enumerate(self):
            if query == product['code']:
                self.pop(index)

    def __search(self):
        if not self:
            print('Object is empty.')
            return
        query = input("Type any beginning of value to find product of it: ").lower()
        results = []
        for product in self:
            for value in product.values():
                if type(value) == str:
                    match = re.search(f"^{query}", value.lower())
                    if match and product not in results:
                        results.append(product)

        display_amount(results)
        display_products(results)
        return results

    def edit(self):
        edit_menu = menu.init(
            ['Display all', 'Add product', 'Delete product', 'Search product'],
            [self.__display, self.__add, self.__delete, self.__search]
        )
        edit_menu.run()


def start():
    db = ProductsDB()
    editable = DBEditor(db)
    editable.edit()
    db.write(editable)


if __name__ == '__main__':
    start()
