#!/bin/python
def print_ar(ar):
    for a in ar:
        print a,
    print ""

def insertionSort(ar):
    for i in xrange(1, len(ar)):
        p = i
        for j in xrange(0, i):
            if ar[j] > ar[p]:
                p = j
                break
        if p != i:
            ar[p], ar[p+1:i + 1] = ar[i], ar[p:i]
        print_ar(ar)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
