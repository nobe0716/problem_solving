# 2022-08-27 18:49:08.959969
# https://codeforces.com/problemset/problem/1616/C
import sys
from collections import Counter

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, a):
    if n == 1:
        return 0
    visited = set()

    res = n
    for i in range(n - 1):
        for j in range(i + 1, n):
            diff = a[j] - a[i]
            distance = j - i
            key = diff / distance
            if key in visited:
                continue
            visited.add(key)

            c = Counter()
            flag = True
            for k in range(n):
                # make it integer operation for performance
                c[distance * a[k] - diff * k] += 1

                if len(c) > res:
                    flag = False
                    break

            if flag:
                v = n - c.most_common(1)[0][1]
                res = min(res, v)
    return res


assert proc(6, [3, -2, 4, -1, -4, 0]) == 3

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = proc(n, a)
    print(ans)
