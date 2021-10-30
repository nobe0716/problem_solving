# https://codeforces.com/problemset/problem/1426/D
import sys
from collections import defaultdict, deque
from typing import List

_DEBUG = False
# _DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def solve(n: int, a: List[int]) -> int:
    sum_idx = defaultdict(lambda: deque())
    sum_idx[0].append(-1)
    ans = 0
    prefix_sum = 0
    last_inserted_position = -2
    for i, e in enumerate(a):
        prefix_sum += e
        if prefix_sum in sum_idx:
            while len(sum_idx[prefix_sum]) > 0 and sum_idx[prefix_sum][0] < last_inserted_position:
                sum_idx[prefix_sum].popleft()

            if len(sum_idx[prefix_sum]) > 0:
                idx = sum_idx[prefix_sum].popleft()
                last_inserted_position = i - 1
                ans += 1
                if _DEBUG:
                    print(i, last_inserted_position)

        sum_idx[prefix_sum].append(i)
    if _DEBUG:
        print(ans)
    return ans


# assert solve(4, [1, -5, 3, 2]) == 1
# assert solve(9, [-1, 1, -1, 1, -1, 1, 1, -1, -1]) == 6
# assert solve(8, [16, -5, -11, -15, 10, 5, 4, -4]) == 3
# assert solve(100, [int(x) for x in '2 1 -2 -1 -2 -1 -2 1 2 1 -2 -1 -2 2 1 -2 -2 2 -2 2 -2 2 2 -1 -2 2 -1 -1 -2 -1 -2 2 -2 -2 -2 -1 1 -2 -1 2 -1 -2 1 -1 1 1 2 -2 1 -2 1 2 2 -2 1 -2 -1 -1 -2 -2 1 -1 -1 2 2 -1 2 1 -1 2 2 1 1 1 -1 -1 1 -2 -2 2 -1 2 -2 2 -2 -1 -2 -2 -1 -1 2 -2 -2 1 1 -2 -1 -2 -2 2'.strip().split()]) == 34

n = int(input().strip())
a = [int(x) for x in input().strip().split()]
ans = solve(n, a)
print(ans)
