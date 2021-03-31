'''
File:        recursive_binary_search.py
Author:      Aniket Patil
Date:        31-03-2021
Description: This code snippet explains how recursive binary search algorithm works using python.

'''


def recursive_binary_search(list, target):

    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print("Target found :", result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)
