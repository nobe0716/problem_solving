__author__ = 'sunghyo.jung'
def partition(ar, l, r, p):
    pv = ar[p]
    ar[r], ar[p] = ar[p], ar[r]
    si = l;
    for i in range(l, r):
        if ar[i] < pv:
            ar[si], ar[i] = ar[i], ar[si]
            si += 1
    ar[r], ar[si] = ar[si], ar[r]
    return si, ar

def find_kth(ar, l, r, k):
    if l == r:
        return ar[l]
    while True:
        pi = (r + l) / 2
        pi, ar = partition(ar, l, r, pi)
        if k == pi:
            return ar[pi]
        elif k <= pi:
            r = pi - 1
        else:
            l = pi + 1


n = int(raw_input())
ar = map(int, raw_input().split())
print(find_kth(ar, 0, n - 1, (n + 1) / 2 - 1))
