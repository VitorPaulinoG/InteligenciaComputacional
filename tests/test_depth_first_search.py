import unittest
from depth_first_search import depth_first_search

class TestDepthFirstSearch(unittest.TestCase):
    def setUp(self):
        self.adjacencias = [
        #    A  B  C  D  E  F  G  H  I  J
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # A
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # B
            [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],  # C
            [0, 1, 1, 1, 0, 0, 1, 0, 0, 0],  # D
            [0, 0, 1, 1, 0, 0, 1, 0, 0, 0],  # E
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],  # F
            [0, 0, 0, 1, 1, 1, 0, 0, 1, 1],  # G
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # H
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],  # I
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],  # J
        ]

    def test_encontrar_caminho(self):
        inicial = 8
        objetivo = 0
        result = depth_first_search(self.adjacencias, inicial, objetivo)
        self.assertEqual(result, [0, 2, 4, 6, 8])
        