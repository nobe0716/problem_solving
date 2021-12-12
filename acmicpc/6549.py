import sys
from typing import List

input = sys.stdin.readline


def solve(n: int, a: List[int]) -> int:
    stack = []
    ans = 0
    for i, e in enumerate(a):
        while stack and stack[-1][2] >= e:
            lo, hi, v = stack.pop()
            ans = max(ans, (i - lo) * v)

        if stack:
            stack.append((stack[-1][1] + 1, i, e))
        else:
            stack.append((0, i, e))

    while stack:
        lo, hi, v = stack.pop()
        ans = max(ans, (n - lo) * v)

    return ans


while True:
    a = input().strip()
    arr = [int(x) for x in a.split()]
    if arr[0] == 0:
        break
    ans = solve(arr[0], arr[1:])
    print(ans)
