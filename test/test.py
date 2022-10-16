import unittest
from functools import reduce

from fileReader import FileReader
from methods import Methods

FILE_PATH = 'file.txt'

class TestMethods(unittest.TestCase):
    data = FileReader(FILE_PATH)
    methods = Methods(data())

    def test_min_function(self):
        self.assertEqual(self.methods._min()['result'], min(self.data()))

    def test_max_function(self):
        self.assertEqual(self.methods._max()['result'], max(self.data()))

    def test_sum_function(self):
        self.assertEqual(self.methods._sum()['result'], sum(self.data()))

    def test_mult_function(self):
        self.assertEqual(self.methods._mult()['result'], reduce(lambda x,y: x*y, self.data()))

    @unittest.expectedFailure
    def test_failure_sum_function(self):
        self.assertEqual(self.methods._sum()['result'], -1)

if __name__ == '__main__':
    unittest.main()