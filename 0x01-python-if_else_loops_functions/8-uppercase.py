#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) >= 97 and ord(s) <= 129:
            up = ord(s) - 32
            print("{}".format(chr(up)), end="")

    print("{}".format(s), end="")
