import polars as pl


def filtrar_mayores(df: pl.DataFrame, columna: str, umbral: float) -> pl.DataFrame:
    """Filtra las filas donde una columna supera un umbral.

    Args:
        df: DataFrame de entrada.
        columna: Nombre de la columna a comparar.
        umbral: Valor mínimo (exclusivo) que debe superar la columna.

    Returns:
        Un nuevo DataFrame solo con las filas que cumplen la condición.
    """
    return df.filter(pl.col(columna) > umbral)


def media_columna(df: pl.DataFrame, columna: str) -> float:
    """Calcula la media de una columna numérica.

    Args:
        df: DataFrame de entrada.
        columna: Nombre de la columna numérica.

    Returns:
        Media aritmética de los valores de la columna.
    """
    return df[columna].mean()
