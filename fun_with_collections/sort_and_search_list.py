"""
Program: sort_and_search_list.py
Author: Colten Pfander
Last date modified: 10/7/2019

The purpose of this program is to use a function search_list() to return the index of the object in the list or a -1
if not found as well as using sort_list() to sort it
"""


def make_list():
    """
    :return: make_list() will call the get_input() function to ask the user for input and then store it inside of
    a list using a for loop, then return that list
    """
    input_list_of_three = []
    try:
        for value in range(0, 3):
            num = int(get_input())
            input_list_of_three.append(num)
        return input_list_of_three
    except ValueError:
        print("Error! Please enter only numbers!")


def get_input():
    """
    :return: get_input() will return a string that collects information from the user that is reusable
    """
    return input("Please enter a number: ")


def sort_list(generic_list):
    # generic_list.sort()  # I'm doing a return statement because it makes it nice and clean to print for the user
    # return generic_list
    pass


def search_list(generic_list):
    # try:
    #     index_input = int(input("Please enter a number you wish to search in the list: "))
    #     index = generic_list.index(index_input)
    #     return 'The index of ' + str(index_input) + ": " + str(index)
    # except ValueError:
    #     return "-1"
    pass


if __name__ == '__main__':
    a_list = make_list()
    print(sort_list(a_list))
    print(search_list(make_list()))
