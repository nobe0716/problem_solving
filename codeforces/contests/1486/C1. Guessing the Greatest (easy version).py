# 2022-03-26 13:54:25.834550
# https://codeforces.com/problemset/problem/1486/C1
from functools import lru_cache
from itertools import permutations
from typing import List

_DEBUG = True
_DEBUG = False


def proc():
    n = int(input().strip())
    l, r = 1, n

    @lru_cache(None)
    def guess(a, b):
        print('? {} {}'.format(a, b))
        return int(input().strip())

    while l != r:
        if r == l + 1:
            x = guess(l, r)
            if x == r:
                r -= 1
            else:
                l += 1
            break
        if r == l + 2:
            x = guess(l, r)
            if x == l:
                if guess(l + 1, r) == l + 1:
                    l = l + 2
                else:
                    l = l + 1
            elif x == l + 1:
                if guess(l, l + 1) == l:
                    l = l + 2
            else:  # x == r
                if guess(l, l + 1) == l:
                    l = l + 1
            break

        ga = guess(l, r)
        mid = (l + r) // 2

        if ga <= mid:
            la = guess(l, mid)
            if la == ga:
                r = mid if la != mid else mid - 1
            else:
                l = mid + 1

        else:  # ga > mid
            ra = guess(mid + 1, r)
            if ra == ga:
                l = (mid + 1) if ra != mid + 1 else mid + 2
            else:
                r = mid
    print('! {}'.format(l))


def find_second_minimum(a: List[int], l, r):
    second_max_v = sorted(a[l:r + 1], reverse=True)[1]
    return a.index(second_max_v)


if _DEBUG:
    n = 4
    mid = (1 + n) // 2

    ga_left_side = []
    ga_right_side = []
    for p in permutations(range(1, n + 1)):
        a = [0] + list(p)
        ga = find_second_minimum(a, 1, n)
        la = find_second_minimum(a, 1, mid)
        ra = find_second_minimum(a, mid + 1, n)
        v = '{} {} {} {}'.format(a[1:], ga, la, ra)
        if ga <= mid:
            ga_left_side.append(v)
        else:
            ga_right_side.append(v)
    print('\n'.join(ga_left_side))
    print('-' * 20)
    print('\n'.join(ga_right_side))
else:
    proc()
