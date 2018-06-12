import types
import unittest

from .generator  import get_first_n_integers
class TestGenerator(unittest.TestCase):
    def test_0(self):
        self.try_with_number(0)

    def test_123456789(self):
        self.try_with_number(123456789)
    
    def try_with_number(self, number):
        gen = get_first_n_integers(number)
        self.assertTrue(type(gen) is types.GeneratorType, "get_first_n_integers' return type is {}, should be {}".format(type, types.GeneratorType))
        self.assertTrue(all(type(x) is int for x in gen), "get_first_n_integers returned something that is not an generator of ints")
        for i, num in enumerate(gen, start=1):
            self.assertTrue(num == i, "{} should be {}, list is not ordered".format(num, i))
