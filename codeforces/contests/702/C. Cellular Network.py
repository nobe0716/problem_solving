# 2022-10-23 19:49:41.538580
# https://codeforces.com/problemset/problem/702/C
import sys

_DEBUG = False
_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, m, a, b):
    def feasible(r):
        bi = 0
        for e in a:
            while bi < m and b[bi] + r < e:
                bi += 1

            if bi == m:
                return False
            elif b[bi] - e > r:
                return False
        return True

    lo, hi = 0, 2 * 10 ** 9
    res = hi
    while lo <= hi:
        r = (lo + hi) // 2
        if feasible(r):
            res = r
            hi = r - 1
        else:
            lo = r + 1

    return res


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = proc(n, m, a, b)
print(ans)
