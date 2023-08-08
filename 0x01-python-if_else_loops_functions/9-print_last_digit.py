#!/usr/bin/python3
def print_last_digit(number):
    s = str(number)
    print("{}".format(int(s[-1])), end="")
    return(int(s[-1]))
