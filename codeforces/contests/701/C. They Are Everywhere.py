# 2022-03-05 16:28:00.255286
# https://codeforces.com/problemset/problem/701/C
import sys
from collections import Counter

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, s):
    def is_feasible(flat_len):
        c = Counter(s[:flat_len])
        if len(c) == types:
            return True
        for i in range(flat_len, n):
            c[s[i]] += 1
            c[s[i - flat_len]] -= 1
            if c[s[i - flat_len]] == 0:
                del c[s[i - flat_len]]

            if len(c) == types:
                return True
        return False

    types = len(set(s))
    lo, hi = types, len(s) - 1
    res = len(s)
    while lo <= hi:
        mid = (lo + hi) // 2
        if is_feasible(mid):
            res = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return res


n = int(input())
s = input().strip()

ans = proc(n, s)
print(ans)
