# 2022-02-27 15:06:41.539062
# https://codeforces.com/problemset/problem/1567/C
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n):
    narr = list(str(n))
    is_odd = True
    odd = ''
    even = ''
    while narr:
        if is_odd:
            odd = narr.pop() + odd
        else:
            even = narr.pop() + even
        is_odd = not is_odd

    odd = int(odd) if odd else 0
    even = int(even) if even else 0

    if even == 0:
        return odd - 1
    else:
        return (odd + 1) * (even + 1) - 2


for _ in range(int(input())):
    n = int(input())
    ans = proc(n)

    print(ans)
