import unittest
import main


class MainTest(unittest.TestCase):

    def test_1(self):
        candies = [2, 3, 5, 1, 3]
        extra_candies = 3
        result = main.main(candies, extra_candies)
        answer = [True, True, True, False, True]
        self.assertEqual(answer, result)

    def test_2(self):
        candies = [4, 2, 1, 1, 2]
        extra_candies = 1
        result = main.main(candies, extra_candies)
        answer = [True, False, False, False, False]
        self.assertEqual(answer, result)

    def test_3(self):
        candies = [12, 1, 12]
        extra_candies = 10
        result = main.main(candies, extra_candies)
        answer = [True, False, True]
        self.assertEqual(answer, result)
