# 2022-08-28 17:35:05.008015
# https://codeforces.com/problemset/problem/1632/C
import math
import sys
from collections import deque

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(a, b):
    if a == b:
        return 0
    elif b == a | b:
        return 1

    res = b - a
    msb = 2 ** int(math.floor(math.log2(b)))
    for ap in range(a, b + 1):
        bit = msb
        bp = 0
        while bit > 0:
            if not ap & bit and b & bit:
                bp += bit
            elif ap & bit and b & bit:
                bp += bit
            elif ap & bit and not b & bit:
                bp += bit
                break
            bit //= 2

        # ap - a + bp - b + ap | bp - bp + 1 = ap + ap | bp - a - b + 1
        res = min(res, ap + (ap | bp) - a - b + 1)
    # print(a, b, res)
    return res


assert proc(56678, 164422) == 23329
assert proc(2, 5) == 2
assert proc(1, 3) == 1
assert proc(5, 8) == 3
assert proc(3, 19) == 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = proc(a, b)
    print(ans)
