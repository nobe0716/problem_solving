# https://codeforces.com/problemset/problem/1499/C
"""
misreading, thought that direction change is not mandatory
"""
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, a):
    ver_min = a[0]
    ver_sum = a[0]
    ver_cnt = 1

    hor_min = a[1]
    hor_sum = a[1]
    hor_cnt = 1

    min_cost = ver_sum + (n - ver_cnt) * ver_min + hor_sum + (n - hor_cnt) * hor_min
    for i in range(2, n):
        e = a[i]
        if i % 2 == 0:
            ver_min = min(ver_min, e)
            ver_sum += e
            ver_cnt += 1

        else:  # hor
            hor_min = min(hor_min, e)
            hor_sum += e
            hor_cnt += 1
        min_cost = min(min_cost, ver_sum + (n - ver_cnt) * ver_min + hor_sum + (n - hor_cnt) * hor_min)
    return min_cost


if _DEBUG:
    assert solve(4, [1, 1, 2, 1, ]) == 8
    assert solve(3, [2, 3, 1, ]) == 13
    assert solve(5, [4, 3, 2, 1, 4, ]) == 19

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = solve(n, a)
    print(ans)
