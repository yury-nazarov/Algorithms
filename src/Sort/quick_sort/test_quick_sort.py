import pytest
from .quick_sort import main


def test_1():
    print("'3 -1 2 -3 1 -2' == '-3 -2 -1 1 2 3'" )
    assert main('3 -1 2 -3 1 -2') == '-3 -2 -1 1 2 3'

def test_2():
    assert main('0 0') != '0 1'


