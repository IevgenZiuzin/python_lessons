class Fraction:
    __reqs = 0

    def __init__(self, a=None, b=None):
        Fraction.__reqs += 1
        self.__a = a
        self.__b = b

    def __str__(self):
        return self.__a / self.__b

    @classmethod
    def counter(cls):
        return f"class instances: {cls.__reqs}"


f = [Fraction() for i in range(5)]
print(Fraction.counter())
