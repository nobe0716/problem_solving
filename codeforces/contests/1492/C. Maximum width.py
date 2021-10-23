# https://codeforces.com/problemset/problem/1492/C
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, m, s, t):
    earliest = [0] * m
    latest = [0] * m

    i = 0
    j = 0
    # earliest[0] = 0
    while j < m:
        while s[i] != t[j]:
            i += 1
        earliest[j] = i
        j += 1
        i += 1

    i = n - 1
    j = m - 1
    while j >= 0:
        while s[i] != t[j]:
            i -= 1
        latest[j] = i
        j -= 1
        i -= 1

    ans = 1
    for i in range(m - 1):
        ans = max(ans, latest[i + 1] - earliest[i])
    return ans


assert solve(5, 3, 'abbbc', 'abc') == 3
assert solve(5, 2, 'aaaaa', 'aa') == 4

n, m = map(int, input().strip().split())
s = input().strip()
t = input().strip()
ans = solve(n, m, s, t)
print(ans)
