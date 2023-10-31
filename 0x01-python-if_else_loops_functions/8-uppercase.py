#!/usr/bin/python3
def uppercase(str):
    while i < len(str):
        c = ord(str[i])
        if c > 96 and c < 123:
            C = c - 32
            str[i] = chr(C)
        i += 1
