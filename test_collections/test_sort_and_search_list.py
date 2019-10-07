import unittest
import fun_with_collections.sort_and_search_list as topic1


class TestList(unittest.TestCase):
    def test_sort_list(self):
        a_list = [3, 1, 2]
        self.assertEqual(topic1.sort_list(a_list), [1, 2, 3])

    def test_search_list_good(self):
        a_list = [3, 1, 2]
        self.assertEqual(topic1.search_list(a_list), "The index of 3: 0")

    def test_search_list_bad(self):
        a_list = [3, 1, 2]
        self.assertEqual(topic1.search_list(a_list), "-1")


if __name__ == '__main__':
    unittest.main()
