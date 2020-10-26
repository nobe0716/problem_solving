from typing import List


def solve(n: int, m: int, a: List[int]):
    return sum(a) == m


for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    r = solve(n, m, a)
    if r:
        print('YES')
    else:
        print('NO')
