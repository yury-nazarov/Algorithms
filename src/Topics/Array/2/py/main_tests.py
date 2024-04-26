import unittest
import main


class MainTests(unittest.TestCase):

    def test_1(self):
        path = "../data/input_1.txt"
        result = 4
        self.assertEqual(result, 4)

    def test_2(self):
        path = "../data/input_1.txt"
        result = 4
        self.assertEqual(result, 3)

