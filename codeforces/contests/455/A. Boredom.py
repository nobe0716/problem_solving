# https://codeforces.com/problemset/problem/455/A
import sys
from collections import Counter, defaultdict

_DEBUG = True
_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, a):
    c = Counter(a)
    t = defaultdict(int)
    t[1] = c[1]
    max_k = max(c.keys())
    for i in range(2, max_k + 1):
        t[i] = max(t[i - 1], t[i - 2] + c[i] * i)

    return max(t.values())


if _DEBUG:
    assert solve(100, list(map(int, '6 6 8 9 7 9 6 9 5 7 7 4 5 3 9 1 10 3 4 5 8 9 6 5 6 4 10 9 1 4 1 7 1 4 9 10 8 2 9 9 10 5 8 9 5 6 8 7 2 8 7 6 2 6 10 8 6 2 5 5 3 2 8 8 5 3 6 2 1 4 7 2 7 3 7 4 10 10 7 5 4 7 5 10 7 1 1 10 7 7 7 2 3 4 2 8 4 7 4 4'.split()))) == 296

n = int(input())
a = list(map(int, input().split()))

ans = solve(n, a)
print(ans)
