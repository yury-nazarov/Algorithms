import unittest
import main


class MainTest(unittest.TestCase):
    def test_1(self):
        arr = [1, 0, 0, 0, 1]
        n = 1
        result = main.main(arr, n)
        self.assertEqual(True, result)

    def test_2(self):
        arr = [0, 0, 1, 0, 1]
        n = 1
        result = main.main(arr, n)
        self.assertEqual(True, result)

    def test_3(self):
        arr = [0]
        n = 1
        result = main.main(arr, n)
        self.assertEqual(True, result)

    def test_50(self):
        arr = [1, 0, 0, 0, 1]
        n = 2
        result = main.main(arr, n)
        self.assertEqual(False, result)

    def test_51(self):
        arr = []
        n = 1
        result = main.main(arr, n)
        self.assertEqual(False, result)

