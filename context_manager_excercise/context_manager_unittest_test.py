import os
import unittest
from .context_manager import call_class_context_manager
from .context_manager import call_function_context_manager

FILE_NAME="hi.txt"
TEXT="hello"


def silent_delete_file(file_path):
    try:
        os.remove(file_path)
    except OSError:
        pass


class TestContextManager(unittest.TestCase):
    def setUp(self):
        silent_delete_file(FILE_NAME)

    def tearDown(self):
        with open(FILE_NAME, "r") as f:
            file_content = f.read()
        self.assertTrue(file_content == TEXT)
        silent_delete_file(FILE_NAME)

    def test_class(self):
        call_class_context_manager(FILE_NAME, TEXT)
        self.assertTrue(os.path.exists(FILE_NAME))

    def test_function(self):
        call_function_context_manager(FILE_NAME, TEXT)
        self.assertTrue(os.path.exists(FILE_NAME))
 