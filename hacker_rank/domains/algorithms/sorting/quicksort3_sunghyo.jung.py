__author__ = 'sunghyo.jujg'

def partition(a, lo, hi):
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i, a
def qsort(a, lo, hi):
    if lo < hi:
        p, a = partition(a, lo, hi)
        print(" ".join(map(str, a)))
        qsort(a, lo, p - 1)
        qsort(a, p + 1, hi)

n = int(input())
a = [int(x) for x in input().split()]
qsort(a, 0, len(a) - 1)
