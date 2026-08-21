import pandera.polars as pa


class Movimientos(pa.DataFrameModel):
    """Esquema de validación para una tabla de movimientos bancarios.

    Columnas a declarar:
    - id_cliente: entero positivo (> 0).
    - importe: float entre -10.000 y 10.000.

    Pista: https://pandera.readthedocs.io/en/stable/polars.html
    """

    # TODO: declarar id_cliente e importe con pa.Field(...)
