# 2022-02-26 23:36:52.603827
# https://codeforces.com/problemset/problem/1551/C
import sys
from collections import Counter

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def proc(n, a):
    counters = [Counter(x) for x in a]
    key_total = 't'
    for c in counters:
        c[key_total] = sum(c.values())

    maximum_count = 0
    for target in 'abcde':
        sorted_counters = sorted(counters, key=lambda x: 2 * x[target] - x[key_total], reverse=True)

        acc_counter = Counter()
        cnt = 0
        for e in sorted_counters:
            acc_counter += e
            if acc_counter[target] * 2 <= acc_counter[key_total]:
                break
            cnt += 1

        maximum_count = max(maximum_count, cnt)
    return maximum_count


# assert proc(5, ['cbdca', 'd', 'a', 'd', 'e']) == 3
# assert proc(3, ['aba', 'abcde', 'aba']) == 2

for _ in range(int(input())):
    n = int(input())
    a = [input().strip() for _ in range(n)]

    ans = proc(n, a)
    print(ans)
