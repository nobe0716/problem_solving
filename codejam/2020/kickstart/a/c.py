# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d40bb
import functools
import math
from typing import List


def solve(n: int, k: int, elements: List[int]) -> int:
    @functools.lru_cache(None)
    def find_k(current_distance, require_distance):
        return int(math.ceil(current_distance / require_distance)) - 1

    gaps = []
    for i in range(n - 1):
        gaps.append(elements[i + 1] - elements[i])

    left, right = 1, max(gaps)

    while left < right:
        pivot = (right + left) // 2
        sum_of_k = sum(find_k(gap, pivot) for gap in gaps)
        if sum_of_k > k:
            left = pivot + 1
        else:
            right = pivot
    return left


for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    exercises = list(map(int, input().split()))
    r = solve(n, k, exercises)
    print('Case #{}: {}'.format(t, r))
