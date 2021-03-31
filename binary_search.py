'''
File:        binary_search.py
Author:      Aniket Patil
Date:        31-03-2021
Description: This code snippet explains how binary search algorithm works using python.

'''


def binary_search(list, target):
    # values assign to first & last
    first = 0
    # It will show the size of list
    last = len(list) - 1
    while first <= last:
        # this will give the whole no
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = binary_search(numbers, 8)
verify(result)

result = binary_search(numbers, 26)
verify(result)
