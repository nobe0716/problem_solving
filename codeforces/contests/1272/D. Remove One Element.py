# https://codeforces.com/problemset/problem/1272/D
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, a):
    t1 = [1] * n
    t2 = [1] * n

    for i in range(1, n):
        if a[i] > a[i - 1]:
            t1[i] = t1[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if a[i] < a[i + 1]:
            t2[i] = t2[i + 1] + 1

    ans = max(max(t1), max(t2))

    for i in range(1, n - 1):
        if a[i - 1] < a[i + 1]:
            ans = max(ans, t1[i - 1] + t2[i + 1])

    return ans


assert solve(5, [1, 2, 5, 3, 4]) == 4
assert solve(5, [1, 2, 3, 4, 5]) == 5

n = int(input().strip())
a = [int(x) for x in input().strip().split()]

print(solve(n, a))
