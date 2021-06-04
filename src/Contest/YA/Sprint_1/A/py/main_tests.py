import unittest
import main


class MainTests(unittest.TestCase):

    def test_1(self):
        path = "../data/input_1.txt"        # -8 -5 -2 7
        result = main.run(path)
        self.assertEqual(result, -183)

    def test_2(self):
        path = "../data/input_2.txt"        # 8 2 9 -10
        result = main.run(path)
        self.assertEqual(result, 40)


if __name__ == '__main__':
    unittest.main()