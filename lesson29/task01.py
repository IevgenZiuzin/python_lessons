import math


class Circle:

    def __init__(self, r):
        if type(r) == int or type(r) == float:
            self.__radius = r
            self.__c = round(2 * math.pi * self.__radius, 3)

    def __repr__(self):
        return self.__radius

    def __str__(self):
        return str(self.__radius)

    def __eq__(self, other):
        if self.__radius == other.__radius:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__c > other.__c:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__c < other.__c:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.__c >= other.__c:
            return True
        else:
            return False

    def __le__(self, other):
        if self.__c <= other.__c:
            return True
        else:
            return False

    def __add__(self, other):
        return self.__radius + other.__radius

    def __sub__(self, other):
        return self.__radius - other.__radius

    def __iadd__(self, other):
        if type(other) == int or type(other) == float:
            self.__radius = self.__radius + other
            return self

    def __isub__(self, other):
        if type(other) == int or type(other) == float:
            self.__radius = self.__radius - other
            return self


c1 = Circle(2)
c2 = Circle(3)

print(f'Circle 1: {c1}')
print(f'Circle 2: {c2}')
print(f'Circle 1 == Circle 2: {c1 == c2}')
print(f'Circle 1 > Circle 2: {c1 > c2}')
print(f'Circle 1 < Circle 2: {c1 < c2}')
c1 += 1
print(f'Circle 1 += 1: {c1}')
c1 -= 1
print(f'Circle 1 -= 1: {c1}')
print(f'Circle 1 + Circle 2: {c1 + c2}')
print(f'Circle 1 - Circle 2: {c1 - c2}')



