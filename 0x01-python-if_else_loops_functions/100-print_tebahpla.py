#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        c_ascii = i
    else:
        c_ascii = i - 32
    print("{}".format(chr(c_ascii)), end="")
