from collections import Counter
from typing import List


def solve(n: int, a: List[int]) -> int:
    c = Counter(a)
    if len(c) == 1:
        return -1

    max_val = max(c.keys())
    if a[0] == max_val:
        i = 0
        while a[i] == max_val:
            i += 1
        return i
    elif a[-1] == max_val:
        i = n - 1
        while a[i] == max_val:
            i -= 1
        return i + 2
    return a.index(max_val) + 1


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    r = solve(n, a)
    print(r)
