#!/usr/bin/python3
for i in range (0, 10):
    for j in range (i, 10):
        if i == 8 and j == 9:
            print("{}{}\n".format(i,j))
        elif i != j:
            print("{}{}, ".format(i,j), end="")
