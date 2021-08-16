# https://codeforces.com/contest/1474/problem/C
from collections import Counter


def solve(n, a):
    def test_with_x(x):
        ca = Counter(a)
        pairs = []
        for k in a:
            if ca[k] <= 0:
                continue
            ca[k] -= 1
            if ca[x - k] == 0:
                return None

            ca[x - k] -= 1
            pairs.append((k, x - k))
            x = k
        return pairs

    # for i in range(len(ka) - 1, )

    # max_a = max(a)
    a = sorted(a, reverse=True)
    v = set()

    for e in a[1:]:
        x = a[0] + e
        if x in v:
            continue
        v.add(x)
        r = test_with_x(x)
        if r:
            return x, r
    return None


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    r = solve(n, a)
    if not r:
        print('NO')
    else:
        print('YES')
        print(r[0])
        print('\n'.join(' '.join(map(str, pair)) for pair in r[1]))
