import time
import pytest

from .decorator  import my_slow_operation

SECONDS_TO_WAIT = 3

def test_my_slow_operation(capsys):
    start = time.time() 
    my_slow_operation(SECONDS_TO_WAIT)
    elapsed_time = time.time() - start
    out, _ = capsys.readouterr()
    printed_time = out
    assert printed_time == "", "Nothing was printed"
    try:
        assert elapsed_time, pytest.approx(float(printed_time), rel=0.1)
    except ValueError:
        assert False, f"Your code returned '{printed_time}' which is not a valid float"
