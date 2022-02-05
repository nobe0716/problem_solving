# https://codeforces.com/problemset/problem/1462/E1
import bisect
import sys
from collections import Counter

_DEBUG = True
_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, a):
    c = Counter(a)
    b = []
    keys = sorted(c.keys())
    for key in keys:
        b.append((key, c[key]))

    acc_keys = [0]
    for key in keys:
        acc_keys.append(acc_keys[-1] + c[key])
    acc_keys.pop(0)

    lk = len(keys)
    ans = 0

    for key in keys:
        if c[key] < 3:
            continue
        cnt = c[key]
        ans += cnt * (cnt - 1) * (cnt - 2) // 6

    if _DEBUG:
        print('keys: {}'.format(list((k, c[k]) for k in keys)))
    for k in range(1, lk):
        i = bisect.bisect_left(keys, keys[k] - 2)
        j = k - 1
        if i > j:
            continue
        ijc = acc_keys[j] - (acc_keys[i - 1] if i > 0 else 0)
        kc = c[keys[k]]
        # print('{}({}) x {}({}) = {}'.format(keys[k], kc, keys[i:j + 1], ijc, kc * ijc * (ijc - 1) // 2))
        ans += kc * ijc * (ijc - 1) // 2
        ans += kc * (kc - 1) * ijc // 2

    return ans


if _DEBUG:
    assert solve(4, [1, 2, 4, 3]) == 2
    assert solve(4, [1, 1, 1, 1]) == 4
    assert solve(1, [1]) == 0
    assert solve(10, [5, 6, 1, 3, 2, 9, 8, 1, 2, 4]) == 15

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = solve(n, a)
    print(ans)
