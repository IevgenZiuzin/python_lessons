from abc import ABC, abstractmethod
import json


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        ...


class Shoes:
    def __init__(self, name=None):
        self.code = None
        self.name = name
        self.gender = None
        self.form = None
        self.color = None
        self.price = None
        self.vendor = None
        self.size = None


class ShoesBuilder1(Builder, ABC):
    def __init__(self) -> None:
        self._product = Shoes()

    @property
    def product(self) -> Shoes:
        return self._product

    def set_code(self, code: str):
        self._product.code = code

    def set_name(self, name: str):
        self._product.name = name

    def set_gender(self, gender: str):
        self._product.gender = gender

    def set_form(self, form: str):
        self._product.form = form

    def set_color(self, color: str):
        self._product.color = color

    def set_price(self, price: float):
        self._product.price = price

    def set_vendor(self, vendor: str):
        self._product.vendor = vendor

    def set_size(self, size: float):
        self._product.size = size


class DB(list):
    __instance = None
    _path = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(DB, cls).__new__(cls)
        return cls.__instance

    def __init__(self, ls: list = None):
        super().__init__()
        if self.__class__._path is not None:
            self._path = self.__class__._path
            self.extend(self.read())
        if ls:
            self.extend(ls)
            self.save()

    def read(self):
        file = open(self._path, 'r')
        content = file.read()
        file.close()
        if len(content) == 0:
            return list()
        else:
            return json.loads(content)

    def write(self, b):
        file = open(self._path, 'w')
        file.write(json.dumps(b))
        file.close()

    def save(self):
        self.write(self)


class ProductsDB(DB):
    _path = 'products.json'
