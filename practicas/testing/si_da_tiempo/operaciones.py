def suma(a: int, b: int) -> int:
    """Devuelve la suma de dos números.

    Args:
        a: Primer sumando.
        b: Segundo sumando.

    Returns:
        Resultado de sumar a y b.
    """
    return a + b


def resta(a: int, b: int) -> int:
    """Devuelve la resta de dos números.

    Args:
        a: Minuendo.
        b: Sustraendo.

    Returns:
        Resultado de restar b a a.
    """
    return a - b


def dividir(a: float, b: float) -> float:
    """Devuelve el resultado de dividir a entre b.

    Args:
        a: Dividendo.
        b: Divisor.

    Returns:
        Resultado de la división.

    Raises:
        ValueError: Si b es 0.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b
