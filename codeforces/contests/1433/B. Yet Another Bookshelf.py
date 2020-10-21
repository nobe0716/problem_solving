from typing import List


def solve(n: int, a: List[int]) -> int:
    while a[-1] == 0:
        a.pop()
    while a[0] == 0:
        a.pop(0)
    return sum(1 - _ for _ in a)


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    r = solve(n, a)
    print(r)
