# https://codeforces.com/contest/1479/problem/A
from functools import lru_cache


@lru_cache(None)
def get_num(idx):
    print('? {}'.format(idx))
    return int(input())


n = int(input())
l, r = 1, n

while l < r:
    m = (l + r) // 2
    v_m, v_r = get_num(m), get_num(m + 1)
    if v_m < v_r:
        r = m
    elif v_m > v_r:
        l = m + 1
print('! {}'.format(l))
