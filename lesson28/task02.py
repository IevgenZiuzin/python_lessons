class Converter:
    __reqs = 0

    @staticmethod
    def cel_to_far(a):
        Converter.__reqs += 1
        return a + 32

    @staticmethod
    def far_to_cel(a):
        Converter.__reqs += 1
        return a - 32

    @classmethod
    def counter(cls):
        return f"class instances: {cls.__reqs}"


print(Converter.cel_to_far(15))
print(Converter.far_to_cel(50))
print(Converter.counter())


