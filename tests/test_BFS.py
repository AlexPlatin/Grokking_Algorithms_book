import unittest
from breadth_first_search import Graph

class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = Graph()
        self.graph.make_graf()
        self.graph.make_deque()

    def test_base(self):
        self.assertEqual(self.graph.search(), "Natasha")

    def tearDown(self) -> None:
        self.graph = None