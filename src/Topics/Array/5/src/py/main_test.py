import unittest
import main


class MainTest(unittest.TestCase):

    def test_1(self):
        nums = [0, 1, 2, 4, 5, 7]
        answer = ["0->2", "4->5", "7"]
        result = main.main(nums)
        self.assertEqual(answer, result)

    def test_2(self):
        nums = [0, 2, 3, 4, 6, 8, 9]
        answer = ["0", "2->4", "6", "8->9"]
        result = main.main(nums)
        self.assertEqual(answer, result)

    def test_3(self):
        nums = []
        answer = []
        result = main.main(nums)
        self.assertEqual(answer, result)

    def test_4(self):
        nums = [-1]
        answer = ["-1"]
        result = main.main(nums)
        self.assertEqual(answer, result)

