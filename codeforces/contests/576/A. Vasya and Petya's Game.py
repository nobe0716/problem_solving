# https://codeforces.com/problemset/problem/576/A
import math
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def solve(n):
    primes = set(range(2, n + 1))
    upper_bound = int(math.ceil(math.sqrt(n))) + 1
    for i in range(2, upper_bound):
        if i not in primes:
            continue
        for j in range(i * 2, n + 1, i):
            primes.discard(j)

    ans = set()
    # while groups:
    for p in primes:
        x = p
        while x <= n:
            ans.add(x)
            x *= p

    return ans


n = int(input())

ans = solve(n)
print(len(ans))
print(' '.join(map(str, ans)))
