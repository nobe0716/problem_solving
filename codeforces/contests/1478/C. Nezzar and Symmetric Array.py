# 2022-09-24 14:55:43.242231
# https://codeforces.com/problemset/problem/1478/C
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write

"""
b1 b2 b3 b4
-b1 -b2 -b3 -b4

         b2 - b1 + b3 - b1 + b4 - b1
b1 + b1 + b2 + b1 + b3 + b1 + b4 + b1

2b1 + 2b2 + 2b3 + 2b4
2(b1 + b2 + b3 + b4)

b2 - b1 +           b3 - b2 + b4 - b2
b2 + b1 + b2 + b2 + b3 + b2 + b4 + b2
2b2 + 2b2 + 2b3 + 2b4
2(b2 + b2 + b3 + b4)

b3 - b1 + b3 - b2 +         - b3 + b4
b3 + b1 + b3 + b2 + b3 + b3 + b3 + b4
2b3 + 2b3 + 2b3 + b4
2(b3 + b3 + b3 + b4)

        + b4 - b3 + b4 - b2 + b4 - b1
b4 + b4 + b4 + b3 + b4 + b2 + b4 + b1
2b4 + 2b4 + 2b4 + 2b4
2 * (b4 + b4 + b4 + b4)
2n * b4 
"""


def proc(n, d):
    d = sorted(d)
    removal = 0
    s = set()
    for i in range(n, 0, -1):
        if d[i * 2 - 1] != d[i * 2 - 2]:
            return False
        v = d[i * 2 - 1]
        if v % 2 == 1:
            return False
        v //= 2
        v -= removal
        if v < 0:
            return False
        if v % i != 0:
            return False

        cur = v // i
        if cur == 0:
            return False
        if cur in s:
            return False
        s.add(cur)
        removal += cur

    return True


assert proc(4, [40, 56, 48, 40, 80, 56, 80, 48]) == False
assert proc(2, [7, 11, 7, 11]) == False
assert proc(1, [1, 1]) == False

for _ in range(int(input())):
    n = int(input())
    d = list(map(int, input().split()))

    ans = proc(n, d)
    print('YES' if ans else 'NO')
