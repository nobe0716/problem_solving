import math
import sys

sys.setrecursionlimit(1000)
_MODER = 10 ** 9 + 7


def solve(n: int, x: int, p: int) -> int:
    def per(lo, hi, small_count, large_count):
        if lo >= hi:
            return math.factorial(small_count + large_count)
        mid = (lo + hi) // 2
        if p == mid:
            return per(mid + 1, hi, small_count, large_count)
        elif p < mid:
            if large_count == 0:
                return 0
            return (large_count * per(lo, mid, small_count, large_count - 1)) % _MODER
        else:  # p > mid
            if small_count == 0:
                return 0
            return (small_count * per(mid + 1, hi, small_count - 1, large_count)) % _MODER

    res = per(0, n, x - 1, n - x)
    # print(res)
    return res


# assert solve(4, 1, 2) == 6
# assert solve(123, 42, 24) == 824071958

n, x, p = map(int, input().split())

r = solve(n, x, p)
print(r)
