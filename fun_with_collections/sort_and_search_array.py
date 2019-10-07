"""
Program: sort_and_search_array.py
Author: Colten Pfander
Last date modified: 10/7/2019

The purpose of this program is to write 2 functions sort_array() and search_array() that will return the index of the
object in the list or -1 if the item is not found as well as sort the array.
"""
from array import array as arr


def sort_array(array):
    list_1 = array.tolist()
    sorted_list = list_1.sort()
    b = arr('i', sorted_list)
    return b


def search_array(generic_array):
    try:
        index_input = int(input("Please enter a number you wish to search in the array: "))
        index = generic_array.index(index_input)
        return 'The index of ' + str(index_input) + ": " + str(index)
    except ValueError:
        return "-1"


if __name__ == '__main__':
    a = arr('i', [3, 1, 2])
    print(sort_array(a))
