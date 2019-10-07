"""
Program: basic_list_exception.py
Author: Colten Pfander
Last date modified: 10/7/2019

The purpose of this program is to declare two functions that will eventually return a list of user input and another
to return just one input as well as adding in more exceptions to catch invalid input.
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
            if 50 < num < 0:
                raise ValueError
            input_list_of_three.append(num)
        return input_list_of_three
    except ValueError:
        print("Error! Please enter only numbers!")


def get_input():
    """
    :return: get_input() will return a string that collects information from the user that is reusable
    """
    return input("Please enter a number: ")


if __name__ == '__main__':
    print(make_list())
