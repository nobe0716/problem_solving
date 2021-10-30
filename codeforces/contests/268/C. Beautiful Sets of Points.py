# https://codeforces.com/problemset/problem/268/C
import math
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline

n, m = map(int, input().split())
ans = []
threshold = min(n, m)
for i in range(threshold + 1):
    ans.append((i, threshold - i))


def verify(points):
    n = len(points)
    for i in range(n - 1):
        for j in range(i + 1, n):
            pi = points[i]
            pj = points[j]
            d2 = (pi[0] - pj[0]) ** 2 + (pi[1] - pj[1]) ** 2
            if math.sqrt(d2) == int(math.sqrt(d2)):
                print(pi, pj)
                assert False


# verify(ans)

print(len(ans))
for x, y in ans:
    print(x, y)
