import sys
from collections import Counter

input = sys.stdin.readline


def solve(n, a):
    c = Counter(a)
    subseta = set()
    subsetb = set()

    for i in range(102):
        if c[i] >= 2:
            subseta.add(i)
            subsetb.add(i)
        elif c[i] == 1:
            subseta.add(i)

    mexa = mexb = 0
    for i in range(102):
        if i not in subseta:
            mexa = i
            break
    for i in range(102):
        if i not in subsetb:
            mexb = i
            break

    return mexa + mexb


# assert solve(4, list(map(int, '0 2 1 5 0 1'.split()))) == 5
# assert solve(3, list(map(int, '0 1 2'.split()))) == 3
# assert solve(4, list(map(int, '0 2 0 1'.split()))) == 4
# assert solve(6, list(map(int, '1 2 3 4 5 6'.split()))) == 0

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    v = solve(n, a)
    print(v)
