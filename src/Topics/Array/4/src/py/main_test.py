import unittest
import main


class MainTest(unittest.TestCase):
    def test_1(self):
        arr = [0, 3, 2, 1]
        result = main.main(arr)
        self.assertEqual(True, result)

    def test_2(self):
        arr = [1, 2, 3, 2, 1]
        result = main.main(arr)
        self.assertEqual(True, result)

    def test_51(self):
        arr = [2, 1]
        result = main.main(arr)
        self.assertEqual(False, result)

    def test_52(self):
        arr = [3, 5, 5]
        result = main.main(arr)
        self.assertEqual(False, result)

    def test_53(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = main.main(arr)
        self.assertEqual(False, result)

    def test_54(self):
        arr = [2]
        result = main.main(arr)
        self.assertEqual(False, result)