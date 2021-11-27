# https://codeforces.com/problemset/problem/165/B
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n: int, k: int) -> bool:
    lo, hi = 1, n

    def is_feasible(v):
        c = 0
        x = 1
        while v >= x:
            c += (v // x)
            x *= k
        return c >= n

    ans = None
    while lo <= hi:
        mid = (lo + hi) // 2
        if is_feasible(mid):
            hi = mid - 1
            ans = mid
        else:
            lo = mid + 1
    if _DEBUG:
        print(n, k, ans)
    return ans


assert solve(11, 2) == 7
assert solve(7, 2) == 4
assert solve(59, 9) == 54
assert solve(1, 9) == 1

n, k = map(int, input().split())

print(solve(n, k))
