#!/usr/bin/python3
"""find a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    sz = len(list_of_integers)
    if sz == 0:
        return None
    left = 0
    right = sz - 1

    while left < right:
        mid = (left + right) / 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
     
