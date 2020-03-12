import unittest


def cadrados(lista):
    """
    Calcula el cadrado de  los numeros
    :param lista:
    :return:
    """
    return [n ** 2 for n in lista]


def cadrado(n):
    """
    Calcula o cadrado do numero pasado
    :param n:
    :return: cadrado don n**2
    """
    return n ** 2


class ProbaCadrados(unittest.TestCase):

    def testCadrados(self):
        l = [0, 1, 2, 3, 4]
        r = cadrados(l)
        self.assertEqual(r, [0, 1, 4, 9, 16])

if __name__=="__main__":
    if __name__ == '__main__':
        unittest.main()
