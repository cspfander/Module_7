"""
Program: file_io_using_tuples.py
Author: Colten Pfander
Last date modified: 10/7/2019

The purpose of this program is to tie together the seemingly unrelated tuple and arbitrary argument list to perform file
input and output
"""


def write_to_file(a_tuple):
    f = open("student_info.txt", "a")
    f.write(str(tuple(a_tuple)) + "\n")
    f.close()


def get_student_info(**kwargs):
    for key, value in kwargs.items():
        student_name = value
    test_score = input("Please enter as many test scores as you wish, or enter -1 to stop: ")
    score_list = [student_name]
    while test_score != "-1":
        score_list.append(test_score)
        test_score = input("Please enter as many test scores as you wish, or enter -1 to stop: ")
        if test_score == "-1":
            break
    student_tuple = tuple(score_list)
    write_to_file(student_tuple)


def read_from_file():
    f = open("student_info.txt", "r")
    line = f.readlines()
    print(line)


if __name__ == '__main__':
    get_student_info(name="Colten")
    get_student_info(name="Luis")
    get_student_info(name="Abby")
    get_student_info(name="Zach")
    read_from_file()
