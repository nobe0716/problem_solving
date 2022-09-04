# 2022-08-28 21:48:29.252397
# https://codeforces.com/problemset/problem/1633/D
import sys
from collections import defaultdict
from functools import lru_cache

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline
    # print = sys.stdout.write


def proc(n, k, b, c):
    """
        dst = src + ceil(src / x)
        dst - src = ceil(src / x)
        dst - src <= ceil(src / x) < dst - src + 1
    """
    cost_table = defaultdict(int)
    cost_table[1] = 0

    def get_ops(src, dst):
        if (src, dst) in cost_table:
            return cost_table[(src, dst)]
        # ops = 0
        q = [1]
        while dst not in cost_table:
            nq = []
            for s in q:
                for i in range(1, s + 1):
                    key = s + s // i
                    if key in cost_table or key > dst:
                        continue
                    cost_table[key] = cost_table[s] + 1
                    nq.append(key)
            q = nq
        return cost_table[dst]

    res = 0
    entries = []
    for i in range(n):
        cost = get_ops(1, b[i])
        reward = c[i]

        if cost == 0:
            res += reward
        else:
            entries.append((reward / cost, -cost, reward))

    entries = sorted(entries, reverse=True)

    for i in range(len(entries)):
        e, c, r = entries[i]
        c = -c

        if k >= c:
            c -= k
            res += r
            if c == 0:
                break
    return res


for _ in range(int(input())):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = proc(n, k, b, c)
    print(ans)
