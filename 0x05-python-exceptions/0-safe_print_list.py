#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nbr = 0
    for elements in my_list:
        try:
            print("{}".format(elements), end="")
            nbr += 1
        except:
            continue
    print()

    return nbr
