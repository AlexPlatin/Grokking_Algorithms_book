import unittest
from dijkstra_algorithm import AlgorithmDijkstra

class TestDijkstra(unittest.TestCase):
    def setUp(self) -> None:
        self.algorithm = AlgorithmDijkstra()
        self.algorithm.set_graph()
        self.algorithm.set_costs_table()
        self.algorithm.set_parents_table()

    def test_simple(self):
        self.assertEqual(self.algorithm.calculate_best_way(), 6)
