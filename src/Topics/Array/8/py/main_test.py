import unittest
import main


class MainTest(unittest.TestCase):

    def test_1(self):
        input_data = [1, 2, 3, 4]
        result = main.main(input_data)
        answer = [1, 3, 6, 10]
        self.assertEqual(answer, result)

    def test_2(self):
        input_data = [1, 1, 1, 1, 1]
        result = main.main(input_data)
        answer = [1, 2, 3, 4, 5]
        self.assertEqual(answer, result)

    def test_3(self):
        input_data = [3, 1, 2, 10, 1]
        result = main.main(input_data)
        answer = [3, 4, 6, 16, 17]
        self.assertEqual(answer, result)

    def test_4(self):
        input_data = [3]
        result = main.main(input_data)
        answer = [3]
        self.assertEqual(answer, result)
