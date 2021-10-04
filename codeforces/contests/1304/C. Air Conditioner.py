# https://codeforces.com/problemset/problem/1304/C
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, m, temperatures):
    temperatures = sorted(temperatures)

    time = 0
    lower_bound = higher_bound = m

    for ti, li, hi in temperatures:
        time_gap = ti - time
        lower_bound = max(li, lower_bound - time_gap)
        higher_bound = min(hi, higher_bound + time_gap)
        time = ti
        if lower_bound > higher_bound:
            return 'NO'

    return 'YES'


for _ in range(int(input())):
    n, m = map(int, input().split())
    temperatures = []
    for _ in range(n):
        temperatures.append([int(x) for x in input().split()])
    ans = solve(n, m, temperatures)
    print(ans)
