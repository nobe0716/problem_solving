# https://codeforces.com/contest/1582/problem/B
import sys
from collections import Counter

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, a):
    c = Counter(a)
    s = sum(a)
    ans = 0
    # if s == 1:
    #     ans += 1

    ans += 2 ** c[0] * c[1]

    return ans


assert solve(2, [1, 0]) == 2

for _ in range(int(input())):
    n = int(input().strip())
    a = [int(x) for x in input().strip().split()]
    print(solve(n, a))
