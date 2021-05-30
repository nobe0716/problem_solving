# https://codeforces.com/contest/1400/problem/C
import sys

input = sys.stdin.readline


def solve(s, x):
    n = len(s)
    origin = [None] * n
    for i in range(n):
        if s[i] == '0':
            if i - x >= 0:
                origin[i - x] = '0'
            if i + x < n:
                origin[i + x] = '0'

    for i in range(n):
        if s[i] == '1':
            is_valid = False
            if i - x >= 0:
                if origin[i - x] is None:
                    origin[i - x] = '1'
                    is_valid = True
                is_valid |= origin[i - x] == '1'
            if i + x < n:
                if origin[i + x] is None:
                    origin[i + x] = '1'
                    is_valid = True
                is_valid |= origin[i + x] == '1'
            if not is_valid:
                return -1

    for i in range(n):
        if origin[i] is None:
            origin[i] = '0'

    return ''.join(origin)


for _ in range(int(input())):
    s = input().strip()
    x = int(input())
    r = solve(s, x)
    print(r)
