'''
File:        linear_search.py
Author:      Aniket Patil
Date:        31-03-2021
Description: This code snippet explains how linear search algorithm works using python.

'''


def linear_search(list, target):
    # arguments that we have to search in the list
    # Returns the index position of target if found, else returns none

    for i in range(0, len(list)):
        if list[i] == target:
            return i

    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)
