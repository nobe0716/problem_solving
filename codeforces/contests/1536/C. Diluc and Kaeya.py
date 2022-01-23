# https://codeforces.com/problemset/problem/1536/C
"""
"""
import math
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, s):
    def get_ab(nd, nk):
        gcd = math.gcd(nd, nk)
        return nd // gcd, nk // gcd

    t = [1] * n
    acc = [None] * n
    acc[0] = (1, 0) if s[0] == 'D' else (0, 1)

    for i in range(1, n):
        acc[i] = (acc[i - 1][0] + 1, acc[i - 1][1]) if s[i] == 'D' else (acc[i - 1][0], acc[i - 1][1] + 1)
        a, b = get_ab(*acc[i])

        for j in range(i - (a + b), -1, -a - b):
            na, nb = acc[j]
            # a:b === na:nb
            if b * na != a * nb:
                continue
            t[i] = t[j] + 1
            break
    # print(t)
    return t


assert solve(3, 'DDK') == [1, 2, 1]
assert solve(9, 'DKDKDDDDK') == [1, 1, 1, 2, 1, 2, 1, 1, 3]
assert solve(6, 'DDDDDD') == [1, 2, 3, 4, 5, 6]
assert solve(4, 'DKDK') == [1, 1, 1, 2]
assert solve(1, 'D') == [1]

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    ans = solve(n, s)
    print(' '.join(map(str, ans)))
