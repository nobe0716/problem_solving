# https://codeforces.com/contest/1469/problem/C
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.buffer.readline


def solve(n, k, a):
    h_min, h_max = a[0], a[0]
    for i in range(1, n):
        h_min = max(h_min - k + 1, a[i])
        h_max = min(h_max + k - 1, a[i] + k - 1)
        if h_min > h_max:
            return 'NO'
    return 'YES' if (h_min <= a[-1] <= h_max) else 'NO'


# assert solve(6, 3, [0, 0, 2, 5, 1, 1, ]) == 'YES'
# assert solve(2, 3, [0, 2, ]) == 'YES'
# assert solve(3, 2, [3, 0, 2, ]) == 'NO'

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [int(x) for x in input().strip().split()]
    ans = solve(n, k, a)
    print(ans)
