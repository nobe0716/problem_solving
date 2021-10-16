# https://codeforces.com/problemset/problem/1419/C
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, x, a):
    if all(v == x for v in a):
        return 0
    if any(v == x for v in a):
        return 1
    elif sum(a) % n == 0 and sum(a) // n == x:
        return 1
    return 2


# assert solve(4, 1, [5, 1, 1, 1]) == 1

for _ in range(int(input())):
    n, x = map(int, input().strip().split())
    a = [int(x) for x in input().strip().split()]
    ans = solve(n, x, a)
    print(ans)
