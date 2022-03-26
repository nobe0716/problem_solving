# 2022-03-26 13:28:07.265919
# https://codeforces.com/problemset/problem/1461/C
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, m, a, experiments):
    threshold = n
    while threshold > 0 and a[threshold - 1] == threshold:
        threshold -= 1
    if threshold == 0:
        return 1.0

    v = 1.0
    for i in range(m):
        if experiments[i][0] >= threshold:
            v *= (1 - experiments[i][1])
    return 1 - v


for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    experiments = []
    for _ in range(m):
        r, p = input().split()
        experiments.append((int(r), float(p)))
    ans = proc(n, m, a, experiments)
    print('{:.6f}'.format(ans))
