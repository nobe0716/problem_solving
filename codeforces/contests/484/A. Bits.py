# 2022-09-04 15:09:14.803217
# https://codeforces.com/problemset/problem/484/A
import sys
from functools import lru_cache

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def get_msb(x):
    v = 1
    while x > 0:
        x //= 2
        v *= 2
    return v // 2


@lru_cache(None)
def get_count(x):
    c = 0
    while x > 0:
        if x % 2:
            c += 1
        x //= 2
    return c


def proc(l, r):
    if l == r:
        ans = l
    elif get_msb(l) < get_msb(r):  # different pairs
        ans = get_msb(r) - 1
    else:
        base = get_msb(l)
        i = base // 2
        while i > 0 and (l & i == r & i):
            if l & i:
                base += i
            i //= 2

        if i >= 1:
            ans = base + i - 1
    if get_count(ans) < get_count(r):
        ans = r
    if get_count(ans) < get_count(l):
        ans = l
    return ans


for _ in range(int(input())):
    l, r = map(int, input().split())
    ans = proc(l, r)
    print(ans)
