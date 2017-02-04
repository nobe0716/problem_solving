#!/bin/python
__author__ = 'sunghyo.jung'

def quickSort(ar):
    if len(ar) <= 1:
        return ar
    pivot = ar[0]
    left = filter(lambda x: x < pivot, ar)
    right = filter(lambda x: x > pivot, ar)
    sorted_list = quickSort(left) + [pivot] + quickSort(right)
    print(" ".join(map(str, sorted_list)))
    return sorted_list
m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)
