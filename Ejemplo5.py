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

    def setUp(self):
        print("preparando a proba")
        self.l = [0, 1, 2, 3, 4]

    def testCadrado(self):
        print("Executando a proba")
        self.assertEqual(cadrados(self.l), [0, 1, 4, 9, 16])

    def tearDown(self):
        print("Destruindo o contexto")
        del self.l


if __name__ == "__main__":
    unittest.main()
