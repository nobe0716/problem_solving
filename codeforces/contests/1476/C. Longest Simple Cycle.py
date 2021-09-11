# https://codeforces.com/contest/1476/problem/C
import sys

_DEBUG = False
# _DEBUG = True
if not _DEBUG:
    input = sys.stdin.buffer.readline


def solve(n, c, a, b):
    t = [0] * (n + 1)
    t[1] = abs(a[1] - b[1]) + 1 + c[1]
    for i in range(2, n):
        if a[i] == b[i]:
            t[i] = 1 + c[i]
        elif a[i] < b[i]:
            t[i] = max(b[i] - a[i] + 1, t[i - 1] - (b[i] - a[i] - 1)) + c[i]
        else:
            t[i] = max(a[i] - b[i] + 1, t[i - 1] - (a[i] - b[i] - 1)) + c[i]
    return max(t)


if _DEBUG:
    assert solve(2, [4, 2], [-1, 2], [-1, 2]) == 3
    assert solve(2, [3, 2], [-1, 1], [-1, 1]) == 3

for _ in range(int(input())):
    n = int(input())
    c = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    ans = solve(n, c, a, b)
    print(ans)
