# 2022-08-20 20:51:58.176175
# https://codeforces.com/problemset/problem/1630/A
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, k):
    def c(x):
        return x ^ (n - 1)

    pairs = []

    if k == 0:
        return [(i, c(i)) for i in range(n // 2)]
    elif k < n - 1:
        pairs = []
        for i in range(1, n // 2):
            if i == k or i == c(k):
                continue
            pairs.append((i, c(i)))
        pairs += [(0, c(k)), (k, n - 1)]
        return pairs
    else:  # k == n - 1
        if n == 4:
            return None
        pairs = [(n - 1, n - 2), (n - 3, 1)]  # (n - 2 + 1) == n - 1
        # among (0, n - 1), (1, n - 2), (2, n - 3) ;  (0, 2,
        pairs += [(0, 2)]  # (c(n - 3), 0)
        for i in range(3, n // 2):
            pairs.append((i, c(i)))

        return pairs


# print('\n'.join(map(str, proc(8, 7))))

for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = proc(n, k)
    if not ans:
        print(-1)
    else:
        for e in ans:
            print(' '.join(map(str, e)))
