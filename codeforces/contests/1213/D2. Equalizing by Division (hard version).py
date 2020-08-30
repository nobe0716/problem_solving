import math
import sys
from collections import Counter
from collections import defaultdict
from typing import List

input = sys.stdin.readline


def get_degree(n: int):
    return int(math.floor(math.log2(n)))


def solve(n: int, k: int, a: List[int]) -> int:
    number_counter = Counter(a)
    # a = sorted(a)
    keys = sorted(number_counter.keys())

    base_number_dict = defaultdict(list)
    for e in keys:
        v = e
        shifts = 0
        while v > 0:
            base_number_dict[v].extend([shifts] * number_counter[e])
            shifts += 1
            v //= 2

    res = float('inf')
    for key in base_number_dict.keys():
        elems = sorted(base_number_dict[key])
        if len(elems) < k:
            continue
        op_count = sum(elems[:k])
        res = min(res, op_count)

    return res


# assert solve(50, 7,
#              [199961, 199990, 199995, 199997, 199963, 199995, 199985, 199994, 199974, 199974, 199997, 199991, 199993,
#               199982, 199991, 199982, 199963, 200000, 199994, 199997, 199963, 199991, 199947, 199996, 199994, 199995,
#               199995, 199990, 199972, 199973, 199980, 199955, 199984, 199998, 199998, 199992, 199986, 199986, 199997,
#               199995, 199987, 199958, 199982, 199998, 199996, 199995, 199979, 199943, 199992, 199993]) == 7
# assert solve(50, 2, [72548, 51391, 1788, 171949, 148789, 151619, 19225, 8774, 52484, 74830, 20086, 51129, 151145, 87650,
#                      108005, 112019, 126739, 124087, 158096, 59027, 34500, 87415, 115058, 194160, 171792, 136832, 1114,
#                      112592, 171746, 199013, 101484, 182930, 185656, 154861, 191455, 165701, 140450, 3475, 160191,
#                      122350, 66759, 93252, 60972, 124615, 119327, 108068, 149786, 8698, 63546, 187913]) == 12
# assert solve(5, 3, [1, 2, 2, 4, 5]) == 1

n, k = map(int, input().split())
a = list(map(int, input().split()))

res = solve(n, k, a)
print(res)
