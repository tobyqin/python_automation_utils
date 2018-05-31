"""
Powered by py.test.
"""
from utils import *
from time import sleep


def ok():
    sleep(1)
    return 'ok'


def not_ok():
    sleep(3)
    raise SystemError('so bad!')


def test_wait_for():
    result = wait_for(ok)
    assert result == 'ok'

    try:
        wait_for(not_ok,timeout=2,poll_time=1)
    except Exception as e:
        expected = "Timeout to wait for 'not_ok()' in 2 seconds. [SystemError]: so bad!"
        assert e.args[0] == expected
