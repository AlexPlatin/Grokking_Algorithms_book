import unittest
from Selection_sort import selection_sort, find_smallest_number


class TestFindSmallest(unittest.TestCase):
    def test_searching_min(self):
        list_values = [7, 6, 5, 34, 12, 5]
        expectation_index = 2
        self.assertEqual(find_smallest_number(list_values), expectation_index)

    def test_assert_value(self):
        with self.assertRaises(TypeError):
            find_smallest_number(1)


class TestSelectionSort(unittest.TestCase):
    def test_simple_work_of_algorithm(self):
        list_values = [2, 3, 56, 34, 77, 34, 23]
        list_expect = [2, 3, 23, 34, 34, 56, 77]
        self.assertEqual(selection_sort(list_values), list_expect)

    def test_noneright_values(self):
        with self.assertRaises(TypeError):
            list_values = [1, "1", 2]
            selection_sort(list_values)


if __name__ == "__main__":
    unittest.main()