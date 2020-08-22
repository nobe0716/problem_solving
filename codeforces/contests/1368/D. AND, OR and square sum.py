import sys
from collections import Counter
from typing import List


def solve(n: int, a: List[int]) -> int:
    base = [2 ** x for x in range(20)]
    c = Counter()
    for e in a:
        for i, b in enumerate(base):
            if e & b > 0:
                c[i] += 1

    r = [0] * n
    for i, b in enumerate(base):
        for j in range(c[i]):
            r[j] |= b
    return sum(x ** 2 for x in r)


# assert solve(5, [991, 143, 445, 903, 399]) == 2241949
# assert solve(1, [123]) == 15129
# assert solve(3, [1, 3, 5]) == 51
# assert solve(2, [349525, 699050]) == 1099509530625

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
