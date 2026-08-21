import polars as pl


def filtrar_mayores(df, columna, umbral):
    return df.filter(pl.col(columna) > umbral)


def media_columna(df, columna):
    return df[columna].mean()
