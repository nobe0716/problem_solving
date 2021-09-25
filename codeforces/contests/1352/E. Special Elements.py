# https://codeforces.com/contest/1352/problem/E
import sys
from collections import Counter

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.buffer.readline


def solve(n, a):
    c = Counter(a)
    s = [0] * n
    s[0] = a[0]

    ans = set()
    for i in range(n - 1):
        v = a[i]
        for j in range(i + 1, n):
            v += a[j]
            if c[v] > 0:
                ans.add(v)
                if _DEBUG:
                    print(a[i:j + 1], v)
    return sum(c[x] for x in ans)


for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    ans = solve(n, a)

    print(ans)
