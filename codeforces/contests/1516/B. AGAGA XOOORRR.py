# https://codeforces.com/problemset/problem/1516/B
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, a):
    a = [0] + a
    acc = [0] * (n + 1)

    for i in range(1, n + 1):
        acc[i] = acc[i - 1] ^ a[i]

    if acc[n] == 0:
        return 'YES'

    visited = set()
    for i in range(1, n):
        alpha = acc[i]
        if alpha in visited:
            continue
        visited.add(alpha)

        beta = acc[n] ^ acc[i]
        if alpha == beta:
            return True
        elif beta != 0:
            continue
        # a[:i] / a[i + 1:j] / a[j + 1:]
        for j in range(i + 1, n):
            beta = acc[j] ^ acc[i]
            if beta != alpha:
                continue

            gamma = acc[n] ^ acc[j]

            if gamma == alpha or gamma == 0:
                return 'YES'
    return 'NO'


# assert solve(3, [962815211, 962815211, 962815211]) == 'YES'
# assert solve(3, [246652649, 246652649, 246652649]) == 'YES'
# assert solve(3, [49072859, 49072859, 49072859]) == 'YES'

for _ in range(int(input())):
    n, a = int(input()), [int(x) for x in input().strip().split()]
    ans = solve(n, a)
    print(ans)
