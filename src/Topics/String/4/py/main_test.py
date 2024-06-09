import unittest
import main


class MainTest(unittest.TestCase):

    def test_1(self):
        input_data = "Hello World"
        result = main.main(input_data)
        answer = 5
        self.assertEqual(answer, result)

    def test_2(self):
        input_data = "   fly me   to   the moon  "
        result = main.main(input_data)
        answer = 4
        self.assertEqual(answer, result)

    def test_3(self):
        input_data = "   on       "
        result = main.main(input_data)
        answer = 2
        self.assertEqual(answer, result)

    def test_4(self):
        input_data = "          "
        result = main.main(input_data)
        answer = 0
        self.assertEqual(answer, result)
