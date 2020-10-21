from collections import defaultdict
from typing import List


def solve(n: int, a: List[int]) -> List:
    gangs = defaultdict(list)
    for i, g in enumerate(a, start=1):
        gangs[g].append(i)
    if len(gangs) == 1:
        return []

    keys = list(gangs.keys())

    mother = gangs[keys[0]][0]
    father = gangs[keys[1]][0]

    r = []
    for key in keys[1:]:
        for e in gangs[key]:
            r.append((mother, e))

    for e in gangs[keys[0]][1:]:
        r.append((father, e))

    return r


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    r = solve(n, a)
    if not r:
        print('NO')
    else:
        print('YES')
        for _ in r:
            print(_[0], _[1])
