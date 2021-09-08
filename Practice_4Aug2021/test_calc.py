import pytest

import calc


def test_substract():
    assert calc.substract(3, 2) == 1



def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(3, 3) == 6