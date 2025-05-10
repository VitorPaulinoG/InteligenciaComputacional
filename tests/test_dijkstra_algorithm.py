import unittest
from dijkstra_algorithm import dijkstra_algorithm
class TestDijkstraAlgorithm(unittest.TestCase):
    def setUp(self):
        self.adjacencias = [
        #     A  B  C  D  E  F  G      
            [ 0, 2, 1, 0, 0, 0, 0],  # A
            [ 2, 0, 0, 3, 0, 0, 0],  # B
            [ 1, 0, 0, 0, 6, 0, 0],  # C
            [ 0, 3, 0, 0, 1, 2, 0],  # D
            [ 0, 0, 6, 1, 0, 0, 1],  # E
            [ 0, 0, 0, 2, 0, 0, 0],  # F
            [ 0, 0, 0, 0, 0, 1, 0],  # G
        ]
    def test_encontrar_caminho(self):
        inicial = 0
        objetivo = 6
        result = dijkstra_algorithm(self.adjacencias, inicial, objetivo)
        print(result)
        # self.assertEqual(result, [0, 2, 4, 6, 8])