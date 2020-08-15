import sys
from typing import List, Tuple

input = sys.stdin.readline


def solve(n: int, a: List[int]) -> Tuple[int, List[int]]:
    t = {}
    p = {}
    maxi_len = 0
    maxi_val = None

    for i in range(n):
        v = a[i]

        if (v - 1) in t:
            t[v] = t[v - 1][0] + 1, i,
            p[i] = t[v - 1][1]
        else:
            t[v] = 1, i, None

        if t[v][0] > maxi_len:
            maxi_len = t[v][0]
            maxi_val = v

    i = t[maxi_val][1]
    indice = []
    while i in p:
        indice.append(i + 1)
        i = p[i]
    indice.append(i + 1)
    return maxi_len, indice[::-1]


n = int(input())
a = list(map(int, input().split()))
maxi_val, indices = solve(n, a)
print(maxi_val)
print(' '.join(map(str, indices)))
