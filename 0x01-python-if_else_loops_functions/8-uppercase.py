#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        c = ord(str[i])
        if c > 96 and c < 123:
            c_to_p = chr(c - 32)
        else:
            c_to_p = str[i]
        print("{}".format(c_to_p), end="")
        i += 1
    print("")
