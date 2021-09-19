import unittest
import main

class MainTests(unittest.TestCase):

    def test_1(self):
        path = "../data/input_1.txt"
        result = main.is_power(path)
        self.assertEqual(result, False)

    def test_2(self):
        path = "../data/input_2.txt"
        result = main.is_power(path)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()