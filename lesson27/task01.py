class Car:
    def __init__(self, model=None, year=None, producer=None, volume=None, color=None, price=None):
        self.__model = model
        self.__year = year
        self.__producer = producer
        self.__volume = volume
        self.__color = color
        self.__price = price

    def set_model(self, v):
        self.__model = v

    def set_year(self, v):
        self.__year = v

    def set_producer(self, v):
        self.__producer = v

    def set_volume(self, v):
        self.__volume = v

    def set_color(self, v):
        self.__color = v

    def set_price(self, v):
        self.__price = v

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_producer(self):
        return self.__producer

    def get_volume(self):
        return self.__volume

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price
