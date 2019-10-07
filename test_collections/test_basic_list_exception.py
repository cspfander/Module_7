import unittest
from unittest.mock import patch
import fun_with_collections.basic_list as topic1


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(topic1.make_list(), [5, 5, 5])

    @patch('fun_with_collections.topic1.get_input', return_value='ab')  # patch function for input
    def test_make_list_non_numeric(self, input):                        # pass input
        with self.assertRaises(ValueError):                             # this is familiar
            topic1.make_list()                                          # call the function!

    @patch('fun_with_collections.topic1.get_input', return_value=-1)
    def test_make_list_below_range(self, input):
        with self.assertRaises(ValueError):
            topic1.make_list()

    @patch('fun_with_collections.topic1.get_input', return_value=51)
    def test_make_list_above_range(self, input):
        with self.assertRaises(ValueError):
            topic1.make_list()


if __name__ == '__main__':
    unittest.main()
