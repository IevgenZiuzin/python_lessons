import json
import pickle


class Fraction:

    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor
        self.result = self.dividend / self.divisor

    def __str__(self):
        return str(self.result)

    @property
    def __dc(self):
        return {'dividend': self.dividend, 'divisor': self.divisor}

    def to_pickle(self, path):
        with open(path, 'wb') as f:
            f.write(pickle.dumps(self.__dc))

    @staticmethod
    def from_pickle(path):
        with open(path, 'rb') as f:
            dc = pickle.loads(f.read())
            return Fraction(dc['dividend'], dc['divisor'])

    def to_json(self, path):
        with open(path, 'w') as f:
            f.write(json.dumps(self.__dc))

    @staticmethod
    def from_json(path):
        with open(path, 'r') as f:
            dc = json.loads(f.read())
            return Fraction(dc['dividend'], dc['divisor'])


def fraction_pack_test():
    filename = 'test_fraction'
    dividend = 10
    divisor = 2
    frac = Fraction(dividend, divisor)
    frac.to_pickle(f'{filename}.pickle')
    frac.to_json(f'{filename}.json')
    if str(frac.from_json(f'{filename}.json')) == str(frac.from_pickle(f'{filename}.pickle')) == str(frac):
        print('Passed')
    else:
        print('Failed')


if __name__ == '__main__':
    fraction_pack_test()
