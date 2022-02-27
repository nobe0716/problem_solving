# 2022-02-27 12:35:39.649431
# https://codeforces.com/problemset/problem/356/A
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline
    print = sys.stdout.write


def proc(n, m, fights):
    t = [0] * (n + 1)

    next = list(range(n + 1))

    def get_next(i):
        if i > n:
            return n + 1
        j = i
        stack = []
        while n >= j != next[j]:
            stack.append(j)
            j = next[j]
        while stack:
            next[stack.pop()] = j
        return next[i]

    for lo, hi, wi in fights:
        i = get_next(lo)
        while i <= hi:
            if i == wi:
                i += 1
            else:
                t[i] = wi
                next[i] = i + 1
            i = get_next(i)
    return t[1:]


n, m = map(int, input().split())
fights = []
for _ in range(m):
    a, b, c = map(int, input().split())
    fights.append((a, b, c))
ans = proc(n, m, fights)
if _DEBUG:
    print(' '.join(map(str, ans)))
else:
    print(' '.join(map(str, ans)) + '\n')
