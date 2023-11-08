#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    nbr = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    past = 0

    for i in range(len(roman_string) - 1, -1, -1):
        if nbr[roman_string[i]] < past:
            res -= nbr[roman_string[i]]
        else:
            res += nbr[roman_string[i]]
        past = nbr[roman_string[i]]

    return res
