import unittest
import main


class MainTest(unittest.TestCase):

    def test_1(self):
        input_data = ""
        result = main.main(input_data)
        answer = ""
        self.assertEqual(answer, result)
