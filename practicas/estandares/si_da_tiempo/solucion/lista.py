def media(numeros: list[float]) -> float:
    """Devuelve la media de una lista de números.

    Args:
        numeros: Lista de valores numéricos.

    Returns:
        Media aritmética de los valores.
    """
    return sum(numeros) / len(numeros)


def maximo(numeros: list[float]) -> float:
    """Devuelve el valor máximo de una lista de números.

    Args:
        numeros: Lista de valores numéricos.

    Returns:
        El mayor valor de la lista.
    """
    return max(numeros)
