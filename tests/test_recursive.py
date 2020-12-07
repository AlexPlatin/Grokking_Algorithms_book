import unittest

from Recursive_tryings import recursive_factorial, loop_factorial, recursive_sum, recursive_max


class Recursive(unittest.TestCase):
    def test_recursive_algorithm(self):
        self.assertEqual(recursive_factorial(5), 120)

    def test_loop_algorithm(self):
        self.assertEqual(loop_factorial(5), 120)


class Recursive_Sum(unittest.TestCase):
    def test_sum_simple_right_values(self):
        self.assertEqual(recursive_sum([1, 2, 3, 4]), 10)

    def test_sum_right_type(self):
        with self.assertRaises(TypeError):
            recursive_sum(1)

class Recursive_max(unittest.TestCase):
    def test_simple_values(self):
        self.assertEqual(recursive_max([1, 7, 5, 3, 8]), 8)

if __name__ == '__main__':
    unittest.main()