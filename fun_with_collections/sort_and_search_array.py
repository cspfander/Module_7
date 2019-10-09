"""
Program: sort_and_search_array.py
Author: Colten Pfander
Last date modified: 10/7/2019

The purpose of this program is to write 2 functions sort_array() and search_array() that will return the index of the
object in the list or -1 if the item is not found as well as sort the array.
"""
import array as arr


def sort_array(a_array):
    unsorted_list = a_array.tolist()
    unsorted_list.sort()
    a_array = arr.array('i', unsorted_list)
    return a_array


def search_array(a_array, value):
    try:
        return 'The index of ' + str(value) + ": " + str(a_array.index(value))
    except ValueError:
        return "-1"


if __name__ == '__main__':
    a = arr.array('i', [3, 1, 2])
    print(sort_array(a))
