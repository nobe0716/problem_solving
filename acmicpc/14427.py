import math
import sys

input = sys.stdin.readline
_DEFAULT = (10 ** 9 + 1, 1)
_GET = lambda x, y: min(x, y)
_SET = lambda i, v: (v, i)

n = int(input())
a = [int(x) for x in input().split()]
a = [_SET(i, v) for i, v in enumerate(a, start=1)]
m = int(input())
BASE = 2 ** math.ceil(math.log(n, 2))

st = [_DEFAULT] * BASE * 2

st[BASE:BASE + n] = a
for i in range(BASE - 1, 0, -1):
    st[i] = _GET(st[i * 2], st[i * 2 + 1])


def get(lo: int, hi: int) -> int:
    lo += BASE - 1
    hi += BASE - 1

    v = _DEFAULT
    while lo < hi:
        if lo % 2 == 1:
            v = _GET(v, st[lo])
            lo += 1
        if hi % 2 == 0:
            v = _GET(v, st[hi])
            hi -= 1
        lo //= 2
        hi //= 2

    if lo == hi:
        v = _GET(v, st[lo])
    return v


def set(i: int, v: int):
    st[BASE + i - 1] = _SET(i, v)
    i = (i + BASE - 1) // 2
    while i > 0:
        st[i] = _GET(st[i * 2], st[i * 2 + 1])
        i //= 2


for _ in range(m):
    line = list(map(int, input().split()))
    if line[0] == 2:
        print(get(1, n)[1])
    else:
        set(line[1], line[2])
