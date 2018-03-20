import time
from io import StringIO
import os
import unittest
from unittest import mock
try:
    from decorator_exercise.decorator  import my_slow_operation
except ImportError:
    from .decorator_exercise.decorator  import my_slow_operation

SECONDS_TO_WAIT = 3

class TestDecorator(unittest.TestCase):
    def test_print(self):
        with mock.patch('sys.stdout', new=StringIO()) as fake_output:
            start = time.time() 
            my_slow_operation(SECONDS_TO_WAIT)
            elapsed_time = time.time() - start
            printed_time = fake_output.getvalue().strip()
            self.assertFalse(printed_time == "", "Nothing was printed")
            try:
                self.assertAlmostEqual(elapsed_time, float(printed_time), 1)
            except ValueError:
                assert False, f"Your code returned '{printed_time}' which is not a valid float"
