#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for array in matrix:
        for i in array:
            if i != array[-1]:
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i), end="")
        print()
