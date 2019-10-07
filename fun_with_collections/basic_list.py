"""
Program: basic_list.py
Author: Colten Pfander
Last date modified: 10/7/2019

The purpose of this program is to declare two functions that will eventually return a list of user input and another
to return just one input.
"""


def make_list():
    input_list_of_three = []
    try:
        for value in range(0, 3):
            num = int(get_input())
            input_list_of_three.append(num)
        return input_list_of_three
    except ValueError:
        print("Error! Please enter only numbers!")


def get_input():
    return input("Please enter a number: ")


if __name__ == '__main__':
    print()
