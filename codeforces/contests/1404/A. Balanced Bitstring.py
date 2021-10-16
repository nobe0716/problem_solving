# https://codeforces.com/problemset/problem/1404/A
import sys
from collections import Counter

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def solve(n: int, k: int, s: str) -> bool:
    s = list(s)
    for i in range(k):
        updated = None
        for j in range(i, n, k):
            if s[j] != '?':
                updated = s[j]
                break
        if updated:
            for j in range(i, n, k):
                if s[j] == '?':
                    s[j] = updated
                elif s[j] != updated:
                    return False

    c = Counter(s[:k])

    return c['1'] <= k // 2 and c['0'] <= k // 2


assert not solve(3, 2, '1?0')

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip()
    print('YES' if solve(n, k, s) else 'NO')
