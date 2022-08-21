# 2022-08-21 20:02:31.190527
# https://codeforces.com/problemset/problem/1553/D
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(s, t):
    i = len(s) - 1
    j = len(t) - 1

    while i >= 0 and j >= 0:
        if j >= 0 and s[i] == t[j]:
            i -= 1
            j -= 1
        else:
            i -= 2

    return j == -1


# assert proc('ababa', 'ba')

for _ in range(int(input())):
    s = input().strip()
    t = input().strip()
    print('YES' if proc(s, t) else 'NO')
