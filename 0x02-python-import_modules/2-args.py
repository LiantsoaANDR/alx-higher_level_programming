#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    i = len(sys.argv) - 1
    print("{} argument".format(i), end="")
    if i > 1:
        print("s", end="")
    if len(sys.argv) < 2:
        print(".")
    else:
        print(":")

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
