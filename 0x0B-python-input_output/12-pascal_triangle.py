#!/usr/bin/python3

"""representing the Pascal’s triangle of n"""


def pascal_triangle(n):
     """returns a list of lists of integers"""
     lst = []
     if n <= 0:
         return []
     for i in range(n):
         lst.append([])
         for j in range(i):
             if len(lst[i]) == 0:
                 lst[i].append(1)
                 continue
             val = lst[i-1][j] + lst[i-1][j-1]
             lst[i].append(val)
         lst[i].append(1)
     return (lst)
