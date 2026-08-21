import pytest

from operaciones import resta, suma


def test_suma():
    assert suma(2, 3) == 5


def test_suma_con_negativos():
    assert suma(-2, 3) == 1


def test_suma_decimales():
    assert suma(0.1, 0.2) == pytest.approx(0.3)


def test_resta():
    assert resta(5, 3) == 2
