#!/usr/bin/python3
for n in range(122, 60, -1):
    if n % 2 == 0:
        i = 0
    else:
        i = 32
    print("{}".format(chr(n - diff)), end="")
