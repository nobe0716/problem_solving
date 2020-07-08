import bisect
from itertools import permutations

get_value = lambda a, b, c: ((a - b) ** 2 + (b - c) ** 2 + (c - a) ** 2)


def find_min(a, b, c):
    v = float('inf')
    ia = 0
    ic = 0
    la = len(a)
    lc = len(c)
    for eb in b:
        ia = min(bisect.bisect_left(a, eb, ia), la - 1)
        ic = min(bisect.bisect_right(c, eb, ic), lc - 1)
        v = min(v, get_value(a[ia], eb, c[ic]), get_value(a[ia - 1], eb, c[ic]))
    return v


def solve(sr, sg, sb):
    if sr & sg & sb:
        return 0
    ar, ag, ab = map(sorted, (sr, sg, sb))
    v = float('inf')
    for a, b, c in permutations([ar, ag, ab]):
        v = min(v, find_min(a, b, c))
    return v


for _ in range(int(input())):
    nr, ng, nb = map(int, input().split())
    sr = set(map(int, input().split()))
    sg = set(map(int, input().split()))
    sb = set(map(int, input().split()))

    v = solve(sr, sg, sb)
    print(v)
