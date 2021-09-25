# https://codeforces.com/contest/1385/problem/D
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, s):
    def rec(lo, hi, ch):
        if lo == hi - 1:
            return 0 if s[lo] == ch else 1
        mid = (lo + hi) // 2
        return min(
            sum(0 if s[i] == ch else 1 for i in range(lo, mid)) + rec(mid, hi, chr(ord(ch) + 1)),
            sum(0 if s[i] == ch else 1 for i in range(mid, hi)) + rec(lo, mid, chr(ord(ch) + 1))
        )

    return rec(0, n, 'a')


for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    ans = solve(n, s)
    print(ans)
