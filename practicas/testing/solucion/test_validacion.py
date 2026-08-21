import polars as pl
import pytest
from pandera.errors import SchemaError

from validacion import Movimientos


def test_datos_validos():
    df = pl.DataFrame({"id_cliente": [1, 2], "importe": [150.50, -32.10]})
    Movimientos.validate(df)


def test_datos_invalidos():
    df = pl.DataFrame({"id_cliente": [1, -2], "importe": [150.50, 50_000.0]})
    with pytest.raises(SchemaError):
        Movimientos.validate(df)
