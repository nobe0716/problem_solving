# 2022-09-17 00:12:13.929721
# https://codeforces.com/problemset/problem/1626/C
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, k, h):
    s = []
    for ki, hi in zip(k, h):
        while s and (ki - s[-1][0]) <= hi:
            s.pop()

        if s and ki - hi < s[-1][1]:
            old_start = s.pop()[0]
            diff = ki - old_start
            s.append((old_start, ki, diff * (diff + 1) // 2))
        else:
            s.append((ki - hi, ki, hi * (hi + 1) // 2))
    return sum(x[2] for x in s)


assert proc(3, [1, 2, 4], [1, 2, 3]) == 10

for _ in range(int(input())):
    n = int(input())
    k = list(map(int, input().split()))
    h = list(map(int, input().split()))

    ans = proc(n, k, h)
    print(ans)
