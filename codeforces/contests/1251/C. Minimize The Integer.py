import sys
from typing import List


def proc(s: str):
    odd = []
    even = []
    for e in map(int, list(s.strip())):
        if e % 2 == 1:
            odd.append(e)
        else:
            even.append(e)
    i = j = 0
    r = []
    while i < len(odd) and j < len(even):
        if odd[i] < even[j]:
            r.append(odd[i])
            i += 1
        else:
            r.append(even[j])
            j += 1
    r = r + odd[i:] + even[j:]
    return ''.join(map(str, r))


def solve(n: int, a: List[str]) -> List[str]:
    return [proc(s) for s in a]


# assert solve(3, ['0709', '1337', '246432']) == ['0079', '1337', '234642']
input = sys.stdin.readline
n = int(input())
a = [input() for _ in range(n)]

print('\n'.join(solve(n, a)))
