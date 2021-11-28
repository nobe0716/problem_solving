import math
import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
base = 2 ** int(math.ceil(math.log2(n)))
st = [0] * base * 2


def get_sum(lo: int, hi: int) -> int:
    if lo == hi:
        return st[lo]
    elif lo > hi:
        return 0

    c = 0
    if lo % 2 == 1:
        c += st[lo]
        lo += 1
    if hi % 2 == 0:
        c += st[hi]
        hi -= 1
    return c + get_sum(lo // 2, hi // 2)


def update_sum(i: int, v: int):
    st[i] = v
    i //= 2
    while i > 0:
        st[i] = st[i * 2] + st[i * 2 + 1]
        i //= 2


for _ in range(m):
    a, b, c = map(int, input().strip().split())
    if a == 0:  # sum
        print(get_sum(base + min(b, c) - 1, base + max(b, c) - 1))
    else:
        update_sum(base + b - 1, c)
