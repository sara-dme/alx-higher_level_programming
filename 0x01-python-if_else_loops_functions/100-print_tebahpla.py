#!/usr/bin/python3
for n in range(122, 96, -1):
    i = 0
    if n % 2 != 0:
        i = 32
    print('{}'.format(chr(n - i)), end="")
