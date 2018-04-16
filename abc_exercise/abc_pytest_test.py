import pytest

from abc_exercise.library import Base
from abc_exercise.user import Derived


def test_base():
    class Dummy(Base):
        pass
    with pytest.raises(TypeError, match=f"Can't instantiate abstract class {Dummy.__name__} with abstract methods baz"):
        dummy = Dummy()

def test_derived():
    with pytest.raises(NotImplementedError):
        Derived()
