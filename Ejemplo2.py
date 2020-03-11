def cadrados(lista):
    """Calcula el cuadrado de los numeros de una lista
    >>> l = [0,1,2,3,4]
    >>> cadrados(l)
    [0, 1, 4, 9, 16]
    """
    return [n ** 2 for n in lista]


def cadrado (n):

    """Calcula o cadrado do número pasado por parametro

    >>> l = [0, 1, 2, 3, 4]
    >>> for n in l:
    ...  cadrado (n)
    0, 1, 4, 9, 16
    4
    :param n: numero
    :return: cadrado do número n**2
    """
    return n ** 2


def _proba():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    _proba()
    print(cadrados([0, 1, 2]))
    print(cadrado(5))
