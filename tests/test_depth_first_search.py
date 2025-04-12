import unittest
from depth_first_search import depth_first_search

class TestDepthFirstSearch(unittest.TestCase):
    def setUp(self):
        self.adjacencias = [
        #    A  B  C  D  E  F
            [0, 1, 1, 0, 0, 0], # A
            [1, 0, 0, 0, 1, 0], # B
            [1, 0, 0, 1, 0, 1], # C
            [0, 0, 1, 0, 1, 0], # D
            [0, 1, 0, 1, 0, 1], # E
            [0, 0, 1, 0, 1, 0], # F
        ]

    def test_encontrar_caminho(self):
        result = depth_first_search(self.adjacencias, 4, 0)
        self.assertEqual(result, [0, 2, 5, 4])
        