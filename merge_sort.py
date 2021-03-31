'''
File:        merge_sort.py
Author:      Aniket Patil
Date:        31-03-2021
Description: This code snippet explains how merge sort algorithm works using python.

'''


def merge_sort(list):
    '''
    sorts a list in asceding order 
    returns a new sorted list
    divide: Find the midpoint of the list & divide into sublists
    conqure: Recursively sort the sublists ccreated in previous steps
    combine: Merge the sorted sublistscreated in previous sublists

    '''
    if len(list) <= 1:
        return list
    # Divide list in sublists
    left_half, right_half = split(list)
    # call merge sort on the list again & again untill we get the single list or empty list
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    # divide the unsorted list at midpoints into sublists returns two sublists left & right
    mid = len(list)//2
    # This will divide list & returns the whole no
    left = list[:mid]
    # slice operator at startit gives the starting index of the list
    right = list[mid:]
    # This will give last index of the list
    return left, right


def merge(left, right):
    '''
    Merges two lists(arrays), sorting them in the process 
    returns a new merged list
    '''
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    return list[0] < list[1] and verify_sorted(list[1:])


alist = [54, 62, 93, 17, 44, 55, 30]
l = merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))
