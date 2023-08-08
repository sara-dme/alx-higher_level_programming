#!/usr/bin/python3
def uppercase(str):
    for s in str:
        ch = ord(s)
        if ch >= 97 and ch <= 129:
            ch = ch - 32
            print("{:c}".format(ch)), end="")

    print()
