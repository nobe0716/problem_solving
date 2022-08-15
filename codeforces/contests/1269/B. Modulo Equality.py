# 2022-08-15 22:51:36.565669
# https://codeforces.com/problemset/problem/1269/B
import sys


def proc(n, m, a, b):
    a = sorted(a)
    b = sorted(b)

    def is_possible(i, x):
        if x < 0:
            return False
        for j in range(n):
            if b[(i + j) % n] != (a[j] + x) % m:
                return False

        return True

    ans = float('inf')

    for i in range(n):
        # j = 0

        if is_possible(i, b[i] - a[0]):
            ans = min(ans, b[i] - a[0])
        elif is_possible(i, b[i] + m - a[0]):
            ans = min(ans, b[i] - a[0] + m)
    return ans


_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = proc(n, m, a, b)
print(ans)
