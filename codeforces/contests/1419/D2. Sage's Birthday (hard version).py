# https://codeforces.com/problemset/problem/1419/D2
import sys
from typing import List

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n: int, a: List[int]):
    if n == 1:
        return 0, a
    a = sorted(a, reverse=True)
    b = [None] * n
    for i in range(1, n, 2):
        b[i] = a.pop()

    k = (n - 1) if n % 2 == 1 else (n - 2)
    while a and a[-1] <= b[1]:
        b[k] = a.pop()
        k -= 2

    for i in range(0, n, 2):
        if b[i] is None:
            b[i] = a.pop()
        else:
            break

    for i in range(n):
        if b[i] is None:
            b[i] = a.pop()

    r = 0
    for i in range(1, n):
        if i < n - 1 and b[i - 1] > b[i] < b[i + 1]:
            r += 1
    return r, b


assert solve(10, [int(x) for x in '1 2 3 3 3 3 3 3 4 5'.split()])[0] == 3

n = int(input())
a = [int(x) for x in input().strip().split()]
r, ans = solve(n, a)
print(r)
print(' '.join(map(str, ans)))
