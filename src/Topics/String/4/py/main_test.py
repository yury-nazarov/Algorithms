import unittest
import main


class MainTest(unittest.TestCase):

    def test_1(self):
        input_data = "PPALLP"
        result = main.main(input_data)
        answer = True
        self.assertEqual(answer, result)

    def test_2(self):
        input_data = "PPALLL"
        result = main.main(input_data)
        answer = False
        self.assertEqual(answer, result)

    def test_3(self):
        input_data = "ALL"
        result = main.main(input_data)
        answer = True
        self.assertEqual(answer, result)

    def test_4(self):
        input_data = "AA"
        result = main.main(input_data)
        answer = False
        self.assertEqual(answer, result)