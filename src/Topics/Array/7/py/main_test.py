import unittest
import main


class MainTest(unittest.TestCase):

    def test_1(self):
        array = [1, 3, 5, 4, 7]
        result = main.main(array)
        answer = 3
        self.assertEqual(answer, result)

    def test_2(self):
        array = [2, 2, 2, 2, 2]
        result = main.main(array)
        answer = 1
        self.assertEqual(answer, result)

    def test_3(self):
        array = [0, 1, 2, 3, 4]
        result = main.main(array)
        answer = 5
        self.assertEqual(answer, result)

    def test_4(self):
        array = [1, 3, 5, 4, 2, 3, 4, 5]
        result = main.main(array)
        answer = 4
        self.assertEqual(answer, result)