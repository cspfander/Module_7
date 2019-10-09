import unittest
import array as arr
import fun_with_collections.sort_and_search_array as topic1


class MyTestCase(unittest.TestCase):
    def test_sort_list(self):
        generic_array = arr.array('i', [3, 1, 2])
        self.assertEqual(topic1.sort_array(generic_array), arr.array('i', [1, 2, 3]))

    def test_search_list_good(self):
        generic_array = arr.array('i', [3, 1, 2])
        self.assertEqual(topic1.search_array(generic_array, 3), "The index of 3: 0")

    def test_search_list_bad(self):
        generic_array = arr.array('i', [3, 1, 2])
        self.assertEqual(topic1.search_array(generic_array, 5), "-1")


if __name__ == '__main__':
    unittest.main()
