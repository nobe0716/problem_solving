# 2022-10-09 17:22:56.547623
# https://codeforces.com/problemset/problem/607/A
import bisect
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, beacons):
    res = n - 1
    t = [0] * n
    beacons = sorted(beacons)
    positions = [beacons[0][0]]
    for i in range(1, n):
        a, b = beacons[i]
        j = bisect.bisect_left(positions, a - b)
        t[i] = (t[j - 1] if j >= 1 else 0) + (i - j)
        broken = n - i - 1
        res = min(res, t[i] + broken)
        positions.append(a)

    return res


n = int(input())
beacons = []
for _ in range(n):
    a, b = map(int, input().strip().split())
    beacons.append((a, b))

ans = proc(n, beacons)
print(ans)
