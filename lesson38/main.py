class NumbCollection:
    def __init__(self):
        self.collection = (1, 2, 3)

    def sum(self):
        return sum(self.collection)

    def average(self):
        if len(self.collection) > 0:
            return sum(self.collection) / len(self.collection)
        else:
            return 0

    def max(self):
        return max(self.collection)

    def min(self):
        return min(self.collection)


class Number(int):
    def __init__(self, number: int):
        super().__init__()
        self.number = number

    def bin(self):
        return bin(self.number)

    def oct(self):
        return oct(self.number)

    def hex(self):
        return hex(self.number)


