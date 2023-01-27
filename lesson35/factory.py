from abc import ABC, abstractmethod


class AbstractCar(ABC):

    @abstractmethod
    def get_body__type(self):
        pass


class SedanCar(AbstractCar):
    def __init__(self):
        self.body = 'sedan'

    def get_body__type(self):
        return f'Body type: {self.body}'


class HatchbackCar(AbstractCar):
    def __init__(self):
        self.body = 'hatchback'

    def get_body__type(self):
        return f'Body type: {self.body}'


class PickupCar(AbstractCar):
    def __init__(self):
        self.body = 'pickup'

    def get_body__type(self):
        return f'Body type: {self.body}'


class CarFactory:
    @staticmethod
    def build_car(type):
        try:
            if type == 'sedan':
                return SedanCar()
            elif type == 'hatchback':
                return HatchbackCar()
            elif type == 'pickup':
                return PickupCar()
            raise AssertionError('Type is not valid')
        except AssertionError as e:
            print(e)


types = ['sedan', 'hatchback', 'pickup', 'truck']
for t in types:
    car = CarFactory.build_car(t)
    print(car)
    print(car.get_body__type())
