# https://www.acmicpc.net/problem/14438
import math
import sys

input = sys.stdin.readline
_MAX = 10 ** 9 + 7
n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
BASE = 2 ** math.ceil(math.log(n, 2))

st = [_MAX] * BASE * 2
st[BASE:BASE + n] = a
for i in range(BASE - 1, 0, -1):
    st[i] = min(st[i * 2], st[i * 2 + 1])


def get(lo: int, hi: int) -> int:
    if lo == hi:
        return st[lo]
    elif lo > hi:
        return _MAX

    v = _MAX
    if lo % 2 == 1:
        v = min(v, st[lo])
        lo += 1
    if hi % 2 == 0:
        v = min(v, st[hi])
        hi -= 1
    return min(v, get(lo // 2, hi // 2))


def set(i: int, v: int):
    st[i] = v
    i //= 2
    while i > 0:
        st[i] = min(st[i * 2], st[i * 2 + 1])
        i //= 2


for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        set(BASE + b - 1, c)
    else:
        print(get(BASE + b - 1, BASE + c - 1))
