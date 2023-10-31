#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3) == 0:
            to_p = "Fizz"
        if (i % 5) == 0:
            to_p = "Buzz"
        if (((i % 3) == 0) and ((i % 5) == 0)):
            to_p = "FizzBuzz"
        if (((i % 3) != 0) and ((i % 5) != 0)):
            to_p = i
        print("{} ".format(to_p), end="")
