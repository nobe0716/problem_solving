"""
## Name of Prob

## Link

## Note

## Input

## Output

## Strategy
"""


def solve(n, k, a):
    possible_range = a[0] - k, a[0] + k
    for i in range(1, n):
        current_range = a[i] - k, a[i] + k

        if possible_range[1] < current_range[0] or possible_range[0] > current_range[1]:
            return -1
        possible_range = max(possible_range[0], current_range[0]), min(possible_range[1], current_range[1])
    return possible_range[1]


_DEBUG = True
q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    r = solve(n, k, a)
    print(r)
