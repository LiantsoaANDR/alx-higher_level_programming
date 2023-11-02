#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    res = 0

    if argc > 1:
        for i in range(1, argc):
            res += int(sys.argv[i])

    print("{}".format(res))
