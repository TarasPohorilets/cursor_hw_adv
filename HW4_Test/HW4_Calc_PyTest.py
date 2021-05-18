from functions_to_test import Calculator as Calc
import pytest


def test_add():
    assert Calc.add(10, 6) == 16
    assert Calc.add(0.14, 0) == 0.14
    assert Calc.add(-9, 3) == -6
    with pytest.raises(TypeError):
        Calc.add("qwerty", 5)
        Calc.add(None, 2)
        Calc.add("2", 8)
        Calc.add([5, 3], 8)


def test_subtract():
    assert Calc.subtract(5, 3) == 2
    assert Calc.subtract(3, 10) == -7
    assert Calc.subtract(-7, 3) == -10
    with pytest.raises(TypeError):
        Calc.subtract(100, "qwerty")
        Calc.subtract("2", 7)
        Calc.subtract(None, 4)
        Calc.subtract({2}, 5)
        Calc.subtract([7, 2], 10)


def test_multiply():
    assert Calc.multiply(8, 4) == 32
    assert Calc.multiply(7, 8) == 56
    assert Calc.multiply(-2, 12) == -24
    with pytest.raises(TypeError):
        Calc.multiply("x", "y")
        Calc.multiply(None, 3)


def test_divide():
    assert Calc.divide(9, 3) == 3
    assert Calc.divide(88, 11) == 8
    assert Calc.divide(-60, 5) == -12
    with pytest.raises(ValueError):
        assert Calc.divide(6, 0)
    with pytest.raises(TypeError):
        Calc.divide(None, 3)
        Calc.divide('qwerty', 5)


if __name__ == '__main__':
    pytest.main()

