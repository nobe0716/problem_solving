import math
import sys

input = sys.stdin.readline

n, q = map(int, input().split())
a = [int(x) for x in input().split()]

BASE = 2 ** int(math.ceil(math.log2(n)))
st = [0] * 2 * BASE
for i in range(n):
    st[BASE + i] = a[i]

for i in range(BASE - 1, 0, -1):
    st[i] = st[i * 2] + st[i * 2 + 1]


def get_sum(x: int, y: int) -> int:
    if x == y:
        return st[x]
    elif x > y:
        return 0
    s = 0
    if x % 2 == 1:
        s += st[x]
        x += 1
    if y % 2 == 0:
        s += st[y]
        y -= 1
    return s + get_sum(x // 2, y // 2)


def update(x: int, v: int):
    st[x] = v
    i = x // 2
    while i > 0:
        st[i] = st[i * 2] + st[i * 2 + 1]
        i //= 2


for _ in range(q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y, = y, x

    print(get_sum(BASE + x - 1, BASE + y - 1))
    update(BASE + a - 1, b)
