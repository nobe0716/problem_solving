# 2022-07-09T15:46:02Z
from functools import lru_cache


def proc(n, k):
    @lru_cache(None)
    def ask(left, right):
        print('? {} {}'.format(left, right))
        v = int(input())
        return v

    lo, hi = 1, n

    while lo < hi:
        # print(lo, hi, k)
        if lo == hi and k == 1:
            return lo
        m = (lo + hi) // 2
        v = ask(lo, m)

        if v == 0 and k == 1:
            return lo

        zero_in_interval = (m - lo + 1) - v

        if zero_in_interval < k:
            k -= zero_in_interval
            lo = m + 1
        elif zero_in_interval > k:
            hi = m - 1
        else:  # zero_in_interval == t -> need to last o
            hi = m
    return lo


n, t = map(int, input().split())
for _ in range(t):
    k = int(input())
    ans = proc(n, k)
    print('! {}'.format(ans))
