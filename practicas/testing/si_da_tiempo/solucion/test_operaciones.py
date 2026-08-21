import pytest

from operaciones import dividir


def test_dividir():
    assert dividir(6, 3) == 2


def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(6, 0)
