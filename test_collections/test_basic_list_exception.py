import unittest
from unittest.mock import patch
import fun_with_collections.basic_list_exception as topic1


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list_exception.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(topic1.make_list(), [5, 5, 5])

    @patch('fun_with_collections.basic_list_exception.make_list', return_value='ab')
    def test_make_list_non_numeric(self, input):
        self.assertRaises(ValueError)

    @patch('fun_with_collections.basic_list_exception.make_list', return_value=-1)
    def test_make_list_below_range(self, input):
        self.assertRaises(ValueError)

    @patch('fun_with_collections.basic_list_exception.make_list', return_value=51)
    def test_make_list_above_range(self, input):
        self.assertRaises(ValueError)


if __name__ == '__main__':
    unittest.main()
