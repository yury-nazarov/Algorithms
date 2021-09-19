import unittest
import main


class MainTests(unittest.TestCase):

    def test_1(self):
        path = "../data/input_1.txt"
        result = main.run(path)
        self.assertEqual(result, ("segment", 7))

    def test_2(self):
        path = "../data/input_2.txt"
        result = main.run(path)
        self.assertEqual(result, ("jumps", 5))

    def test_3(self):
        path = "../data/input_3.txt"
        result = main.run(path)
        self.assertEqual(result, ("sybtbv", 6))


if __name__ == '__main__':
    unittest.main()