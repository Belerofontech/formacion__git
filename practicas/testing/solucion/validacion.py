import pandera.polars as pa


class Movimientos(pa.DataFrameModel):
    """Esquema de validación para una tabla de movimientos bancarios."""

    id_cliente: int = pa.Field(gt=0)
    importe: float = pa.Field(ge=-10_000, le=10_000)
