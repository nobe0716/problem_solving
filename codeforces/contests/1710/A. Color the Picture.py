# 2022-10-16 21:43:25.480766
# https://codeforces.com/problemset/problem/1710/A
import sys

_DEBUG = False
# _DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    print = sys.stdout.write


def proc(n, m, k, a):
    def test_row():
        row = 0
        flag = False
        for i in range(k):
            diff = a[i] // m
            if diff < 2:
                continue
            if diff > 2:
                flag = True
            row += diff
        return row >= n and (n % 2 == 0 or flag)

    def test_col():
        col = 0
        flag = False
        for i in range(k):
            diff = a[i] // n
            if diff < 2:
                continue
            if diff > 2:
                flag = True
            col += diff
        return col >= m and (m % 2 == 0 or flag)

    # a = sorted(a)

    if test_row():
        return True
    return test_col()


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = proc(n, m, k, a)
    if _DEBUG:
        print('Yes' if ans else 'No')
    else:
        print('Yes\n' if ans else 'No\n')
