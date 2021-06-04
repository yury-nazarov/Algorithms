import unittest
import main


class MainTests(unittest.TestCase):

    def test_1(self):
        path = "../data/input_1.txt"    # A man, a plan, a canal: Panama
        result = main.is_palindrome(path)
        self.assertEqual(result, True)

    def test_2(self):
        path = "../data/input_2.txt"    # zo
        result = main.is_palindrome(path)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()