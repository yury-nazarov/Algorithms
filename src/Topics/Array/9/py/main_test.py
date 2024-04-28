import unittest
import main


class MainTest(unittest.TestCase):

    def test_1(self):
        input_data = [1, 2, 2, 3]
        result = main.main(input_data)
        answer = True
        self.assertEqual(answer, result)

    def test_2(self):
        input_data = [6, 5, 4, 4]
        result = main.main(input_data)
        answer = True
        self.assertEqual(answer, result)

    def test_3(self):
        input_data = [1, 3, 2]
        result = main.main(input_data)
        answer = False
        self.assertEqual(answer, result)

    def test_4(self):
        input_data = [1, 1, 1]
        result = main.main(input_data)
        answer = True
        self.assertEqual(answer, result)

    def test_5(self):
        input_data = [1, 1, 1, 2, 2, 2]
        result = main.main(input_data)
        answer = True
        self.assertEqual(answer, result)

    def test_6(self):
        input_data = [1, 1, 1, 2, 2, 2, 1]
        result = main.main(input_data)
        answer = False
        self.assertEqual(answer, result)

    def test_7(self):
        input_data = [1]
        result = main.main(input_data)
        answer = True
        self.assertEqual(answer, result)
