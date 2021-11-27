# https://codeforces.com/problemset/problem/1278/B
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def solve(a, b):
    def is_feasible(v):
        sum_to_v = v * (v + 1) // 2
        if sum_to_v < diff:
            return False
        return sum_to_v % 2 == diff % 2

    diff = abs(a - b)
    v = 0
    while not is_feasible(v):
        v += 1
    return v


for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = solve(a, b)
    print(ans)
