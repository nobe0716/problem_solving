# https://codeforces.com/contest/1393/problem/C
import sys
from collections import Counter

_DEBUG = False
# _DEBUG = True
if not _DEBUG:
    input = sys.stdin.buffer.readline


def solve(n, a):
    c = Counter(a)
    entries = c.most_common()
    a = [None] * n

    def verify(mid: int) -> bool:
        for i in range(n):
            a[i] = None

        loop = 0
        i = 0
        for k, v in entries:
            if mid * (v - 1) + v > n:
                return False
            for _ in range(v):
                if a[i] is not None:
                    return False
                a[i] = k
                i += (mid + 1)
                if i >= n:
                    loop += 1
                    i = loop
        d = {}
        for i, e in enumerate(a):
            if e in d and i - d[e] < mid:
                return False
            d[e] = i
        return True

    lo, hi = 0, n - 1
    res = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if verify(mid):
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return res


if _DEBUG:
    assert solve(7, [1, 7, 1, 6, 4, 4, 6]) == 3
    assert solve(8, [1, 1, 4, 6, 4, 6, 4, 7, ]) == 2
    assert solve(3, [3, 3, 3, ]) == 0
    assert solve(6, [2, 5, 2, 3, 1, 4, ]) == 4

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = solve(n, a)
    print(ans)
