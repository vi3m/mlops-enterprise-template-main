import pytest
from src.entry import add


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-2, 3) == 1


def test_add_zero():
    assert add(0, 3) == 3


def test_add_type_error():
    with pytest.raises(TypeError):
        add("a", 3)


def test_add_multiple_inputs():
    inputs = [
        (1, 2, 3),
        (10, 20, 30),
        (-5, 5, 0),
    ]
    for a, b, expected in inputs:
        assert add(a, b) == expected