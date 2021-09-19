import unittest
import main


class MainTests(unittest.TestCase):

    def test_1(self):
        path = "../data/input_1.txt"
        result = main.list_form(path)
        self.assertEqual(result, "1 2 3 4")

    def test_2(self):
        path = "../data/input_2.txt"
        result = main.list_form(path)
        self.assertEqual(result, "1 1 2")


if __name__ == '__main__':
    unittest.main()