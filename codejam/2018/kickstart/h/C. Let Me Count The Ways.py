import math
import sys

_MOD_BASE = 1000000007

sys.setrecursionlimit(10000)

num_of_tests = int(input())
t = {}
for test_num in range(1, num_of_tests + 1):
    # i non-newled people, j newled couples
    def sol(i, j, k):

        if i == 0 and j == 0:
            return 1
        if j == 0:
            if k == 0:
                return math.factorial(i)
            else:
                return (i - 1) * math.factorial(i - 1)
        if (i, j, k) in t:
            return t[(i, j, k)]
        r = 0
        if j > 0:
            r += (2 * j * sol(i + 1, j - 1, 1))
        if k == 0:
            if i > 0:
                r += (i * sol(i - 1, j, 0))
        else:
            if i > 1:
                r += ((i - 1) * sol(i - 1, j, 0))
        t[(i, j, k)] = r % _MOD_BASE
        # print(i, j, k, ' => ', r)
        return r


    n, m = map(int, input().split())
    # t = [[[0, 0] for _ in range(m + 1)] for _ in range(n + 1)]
    # t[0][0] = 1
    # for i in range(n + 1):
    #     for j in range(m):
    #         t[i][j][0] = i * t[i - 1][j][0] + 2 * j * t[]
    r = sol(2 * (n - m), m, 0) % _MOD_BASE
    print('Case #{}: {}'.format(test_num, r))
