# 2022-07-03T12:03:04Z
import itertools
import sys

input = sys.stdin.readline


def proc(n, a):
    res = 0
    for i in range(n):
        # print([a[i]])
        res += 1
        if i + 1 >= n:
            continue
        # print(a[i:i + 2])
        res += 1

        if i + 2 >= n or a[i] <= a[i + 1] <= a[i + 2] or a[i] >= a[i + 1] >= a[i + 2]:
            continue
        # print(a[i:i + 3])
        res += 1

        if i + 3 >= n \
                or a[i] <= a[i + 1] <= a[i + 3] or a[i] <= a[i + 2] <= a[i + 3] or a[i + 1] <= a[i + 2] <= a[i + 3] \
                or a[i] >= a[i + 1] >= a[i + 3] or a[i] >= a[i + 2] >= a[i + 3] or a[i + 1] >= a[i + 2] >= a[i + 3]:
            continue
        # print(a[i:i + 4])
        res += 1

    # print(res)
    return res


assert proc(5, [6, 9, 1, 9, 6, ]) == 12
assert proc(4, [2, 4, 1, 3, ]) == 10
assert proc(2, [13, 37, ]) == 3
for _ in range(int(input().strip())):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    ans = proc(n, a)
    print(ans)
