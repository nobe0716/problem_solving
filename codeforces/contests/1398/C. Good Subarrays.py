# https://codeforces.com/contest/1398/problem/C
import sys
from collections import defaultdict

input = sys.stdin.readline


def solve(n, a):
    a = list(map(int, a))
    res = 0
    s = 0
    t = defaultdict(int)
    t[0] = 1
    for i in range(n):
        s += a[i]
        x = s - i - 1
        t[x] += 1
        res += (t[x] - 1)
    return res


# assert solve(100_000, '1' * 100_000)
# assert solve(5, '11011') == 6
assert solve(3, '120') == 3
# assert solve(6, '600005') == 1

for _ in range(int(input())):
    n = int(input())
    a = input().strip()
    r = solve(n, a)
    print(r)
