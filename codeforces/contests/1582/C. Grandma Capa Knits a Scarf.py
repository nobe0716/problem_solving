# https://codeforces.com/contest/1582/problem/C
import string
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, s):
    def verify(s: str, ch):
        v = s.replace(ch, '')
        if v != v[::-1]:
            return None
        lo, hi = 0, len(s) - 1
        c = 0
        while lo < hi:
            while lo < hi and s[lo] == s[hi]:
                lo, hi = lo + 1, hi - 1
            if lo >= hi:
                break
            c += 1
            if s[lo] == ch:
                lo += 1
            elif s[hi] == ch:
                hi -= 1
        return c

    if s == s[::-1]:
        return 0
    ans = float('inf')
    for ch in string.ascii_lowercase:
        r = verify(s, ch)
        if r:
            ans = min(ans, r)
    return ans if ans != float('inf') else -1


for _ in range(int(input())):
    n = int(input().strip())
    s = input().strip()
    print(solve(n, s))
