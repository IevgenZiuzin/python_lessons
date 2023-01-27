import unittest
from main import NumbCollection, Number


class NumbCollectionTestCase(unittest.TestCase):
    def setUp(self):
        self.collection = NumbCollection()

    def test_sum(self):
        self.assertEqual(self.collection.sum(), 6)

    def test_average(self):
        self.assertEqual(self.collection.average(), 2)

    def test_max(self):
        self.assertEqual(self.collection.max(), 3)

    def test_min(self):
        self.assertEqual(self.collection.min(), 1)


class NumberTestCase(unittest.TestCase):
    def setUp(self):
        self.test_number = 3
        self.number = Number(self.test_number)

    def test_bin(self):
        self.assertEqual(self.number.bin(), bin(self.test_number))

    def test_oct(self):
        self.assertEqual(self.number.oct(), oct(self.test_number))

    def test_hex(self):
        self.assertEqual(self.number.hex(), hex(self.test_number))
