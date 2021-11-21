import math
import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
BASE = 2 ** math.ceil(math.log2(n))
_M = 10 ** 9 + 7

sa = [1] * (BASE * 2)  # arr


def update(i: int, v: int):
    sa[i] = v
    i //= 2
    while i > 0:
        sa[i] = (sa[i * 2] * sa[i * 2 + 1]) % _M
        i //= 2


def query(lo: int, hi: int):
    if lo == hi:
        return sa[lo]
    elif lo > hi:
        return 1

    b = 1
    if lo % 2 == 1:
        b *= sa[lo]
        lo += 1
    if hi % 2 == 0:
        b *= sa[hi]
        hi -= 1
    return b * query(lo // 2, hi // 2) % _M


for i in range(BASE, BASE + n):
    update(i, arr[i - BASE])

for _ in range(m + k):
    a, b, c = map(int, input().split())
    b += BASE - 1
    if a == 1:
        update(b, c)
    else:
        c += BASE - 1
        print(query(b, c))
