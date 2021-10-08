# https://codeforces.com/problemset/problem/1542/B
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, a, b):
    k = 1
    nmb = n % b
    s = set()
    while k <= n:
        # k %= b
        if k % b == nmb:
            return True
        elif k % b in s:
            return False
        s.add(k % b)
        k *= a
    return False


assert solve(141504991, 37, 25) == False

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    ans = solve(n, a, b)
    print('YES' if ans else 'NO')
