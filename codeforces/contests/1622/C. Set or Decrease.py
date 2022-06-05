# 2022-06-04T21:40:20Z
import math
import sys

_DEBUG = False

if not _DEBUG:
    input = sys.stdin.readline
    print = sys.stdout.write


def proc(n, k, a):
    a = sorted(a, reverse=True)
    sa = sum(a)
    if sa <= k:
        return 0

    ans = sa - k
    initial_diff = 0
    for i in range(n - 1):
        initial_diff += (a[i] - a[-1])
        cost = int(math.ceil(max(0, sa - initial_diff - k) / (i + 2))) + (i + 1)

        if ans > cost:
            ans = cost

    return ans


assert proc(5, 6, [1, 4, 1, 1, 1]) == 1
# assert proc(1, 10, [20]) == 10
# assert proc(7, 8, list(map(int, '1 2 1 3 1 2 1'.split()))) == 2
# assert proc(5, 1, list(map(int, '1 1 1 1 1'.split()))) == 3
# assert proc(10, 1, list(map(int, '1 2 3 1 2 6 1 6 8 10'.split()))) == 7

for _ in range(int(input().strip())):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    ans = proc(n, k, a)
    if _DEBUG:
        print(ans)
    else:
        print(str(ans) + '\n')
