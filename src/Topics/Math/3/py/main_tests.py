import unittest
import main


class MainTest(unittest.TestCase):

    def test_1(self):
        path = "../data/input_1.txt"  # 5
        result = main.to_bin(path)
        self.assertEqual(result, "101")

    def test_2(self):
        path = "../data/input_2.txt"  # 14
        result = main.to_bin(path)
        self.assertEqual(result, "1110")


if __name__ == '__main__':
    unittest.main()