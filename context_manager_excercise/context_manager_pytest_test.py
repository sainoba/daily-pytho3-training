import os
import pytest
from .context_manager import call_class_context_manager
from .context_manager import call_function_context_manager

FILE_NAME="hi.txt"
TEXT="hello"


def silent_delete_file(file_path):
    try:
        os.remove(file_path)
    except OSError:
        pass


class TestClass:
    @pytest.fixture(autouse=True)
    def prepare_text_file(self):
        silent_delete_file(FILE_NAME)
        yield
        with open(FILE_NAME, "r") as f:
            file_content = f.read()
        assert file_content == TEXT
        silent_delete_file(FILE_NAME)

    def test_class(self):
        call_class_context_manager(FILE_NAME, TEXT)
        assert os.path.exists(FILE_NAME)

    def test_function(self):
        call_function_context_manager(FILE_NAME, TEXT)
        assert os.path.exists(FILE_NAME)
