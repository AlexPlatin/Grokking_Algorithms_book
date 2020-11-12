import unittest
from Binary_search import binary_search
from Binary_search import recursive_binary_search


class BinaryTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print()

    def test_first_simple_case(self):
        values = [1, 2, 3, 4, 5, 6, 7]
        item = 3
        predict_index = 2
        self.assertEqual(predict_index, binary_search(values, item))

    def test_second_simple_case(self):
        values = [1, 2, 3, 4, 5, 6]
        item = 4
        predict_index = 3
        self.assertEqual(predict_index, binary_search(values, item))

    def test_recursive_binary_search(self):
        values = [1, 2, 3, 4, 5, 6, 7]
        item = 3
        predict_index = 2
        self.assertEqual(predict_index, recursive_binary_search(values, item, 0, len(values) - 1))

    def test_recursive_binary_search_2(self):
        values = [1, 2, 3, 4, 5, 6]
        item = 1
        predict_index = 0
        self.assertEqual(predict_index, recursive_binary_search(values, item, 0, len(values) - 1))