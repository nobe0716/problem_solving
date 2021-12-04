import math
import sys

input = sys.stdin.readline
_DEFAULT = 0
_OP = lambda x, y: x + y

n, q = map(int, input().split())
BASE = 2 ** math.ceil(math.log(n, 2))

st = [_DEFAULT] * BASE * 2


def get(lo: int, hi: int) -> int:
    if lo == hi:
        return st[lo]
    elif lo > hi:
        return _DEFAULT

    v = _DEFAULT
    if lo % 2 == 1:
        v = _OP(v, st[lo])
        lo += 1
    if hi % 2 == 0:
        v = _OP(v, st[hi])
        hi -= 1
    return _OP(v, get(lo // 2, hi // 2))


def set(i: int, v: int):
    st[i] += v
    i //= 2
    while i > 0:
        st[i] = _OP(st[i * 2], st[i * 2 + 1])
        i //= 2


for _ in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        set(BASE + b - 1, c)
    else:
        print(get(BASE + b - 1, BASE + c - 1))
