import unittest
from Quick_sort import quicksort


class Quicksort_test(unittest.TestCase):
    def test_right_result(self):
        values = [2, 3, 6, 5, 8, 1, 5, 4, 3]
        expect_values = [1, 2, 3, 3, 4, 5, 5, 6, 8]
        self.assertEqual(quicksort(values), expect_values)