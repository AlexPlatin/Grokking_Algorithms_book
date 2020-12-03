import unittest

from Recursive import recursive_factorial, loop_factorial


class Recursive(unittest.TestCase):
    def test_recursive_algorithm(self):
        self.assertEqual(recursive_factorial(5), 120)

    def test_loop_algorithm(self):
        self.assertEqual(loop_factorial(5), 120)


if __name__ == '__main__':
    unittest.main()