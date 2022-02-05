# https://codeforces.com/contest/1562/problem/C
import sys

# 2113
_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, s):
    if '0' not in s:
        return '{} {} {} {}'.format(1, n // 2 * 2, 1, n // 2)
    pos_of_zero = s.index('0')
    if pos_of_zero < n // 2:
        return '{} {} {} {}'.format(pos_of_zero + 1, n, pos_of_zero + 2, n)
    return '{} {} {} {}'.format(1, pos_of_zero + 1, 1, pos_of_zero)


for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = solve(n, s)
    print(ans)
