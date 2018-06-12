import types
import pytest

from .generator  import get_first_n_integers

@pytest.mark.parametrize("number", [
    0,
    123456789,
])
def test_get_first_n_integers(number):
    gen = get_first_n_integers(number)
    assert type(gen) is types.GeneratorType, "get_first_n_integers' return type is {}, should be {}".format(type, types.GeneratorType)
    assert all(type(x) is int for x in gen), "get_first_n_integers returned something that is not an generator of ints"
    for i, num in enumerate(gen, start=1):
        assert num == i, "{} should be {}, list is not ordered".format(num, i)
