# 2022-03-05 16:16:47.392693
# https://codeforces.com/problemset/problem/584/B
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n):
    return (3 ** (3 * n) - 7 ** n) % (10 ** 9 + 7)


assert proc(1) == 20
assert proc(2) == 680
assert proc(3) == 19340
assert proc(4) == 529040
assert proc(5) == 14332100
assert proc(7) == 459529590

n = int(input())
print(proc(n))
