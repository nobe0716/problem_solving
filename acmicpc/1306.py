import math
import sys

input = sys.stdin.readline


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


_DEFAULT = 0
_GET = lambda x, y: max(x, y)
_SET = lambda i, v: v
# _INPUT_TYPE = 'N'
_INPUT_TYPE = 'NM_TOGETHER'

if _INPUT_TYPE == 'NM_TOGETHER':
    n, m = map(int, input().split())
else:
    n = int(input())
a = [int(x) for x in input().split()]
a = [_SET(i, v) for i, v in enumerate(a)]
if _INPUT_TYPE != 'NM_TOGETHER':
    m = int(input())
BASE = 2 ** math.ceil(math.log(n, 2))

st = [_DEFAULT] * BASE * 2

st[BASE:BASE + n] = a
for i in range(BASE - 1, 0, -1):
    st[i] = _GET(st[i * 2], st[i * 2 + 1])

ans = []
for i in range(m, n - m + 2):
    ans.append(get(i - m + 1, i + m - 1))

print(' '.join(map(str, ans)))
