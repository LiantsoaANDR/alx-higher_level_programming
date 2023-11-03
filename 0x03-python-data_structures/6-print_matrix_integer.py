#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for array in matrix:
        for i in array:
            if i != array[-1]:
                print("{}".format(i), end=" ")
            else:
                print("{}".format(i), end="")
        print()
