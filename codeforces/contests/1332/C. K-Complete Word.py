# https://codeforces.com/problemset/problem/1332/C
import sys
from collections import Counter

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, k, s):
    cnt = 0

    for i in range(k):
        c = Counter()
        for j in range(i, n, k):
            c[s[j]] += 1
        for j in range(n - i - 1, -1, -k):
            c[s[j]] += 1
        cnt += (sum(c.values()) - c.most_common(1)[0][1])

    return cnt // 2


for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ans = solve(n, k, s)
    print(ans)
