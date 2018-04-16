#abc_unittest_test.py

import unittest

from .library import Base
from .user import Derived



class TestContextManager(unittest.TestCase):
    def test_base(self):
        class Dummy(Base):
            pass
        with self.assertRaisesRegex(TypeError, f"Can't instantiate abstract class {Dummy.__name__} with abstract methods baz"):
            dummy = Dummy()

    def test_derived(self):
        with self.assertRaises(NotImplementedError):
            Derived()
