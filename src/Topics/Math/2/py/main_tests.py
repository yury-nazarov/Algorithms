import unittest
import main


class MainTests(unittest.TestCase):

    def test_1(self):
        path = "../data/input_1.txt"  # 1 2 -3
        result = main.run(path)
        self.assertEqual(result, "FAIL")

    def test_2(self):
        path = "../data/input_2.txt"  # 7 11 7
        result = main.run(path)
        self.assertEqual(result, "WIN")

    def test_3(self):
        path = "../data/input_3.txt"  # 6 -2 0
        result = main.run(path)
        self.assertEqual(result, "WIN")


if __name__ == '__main__':
    unittest.main()