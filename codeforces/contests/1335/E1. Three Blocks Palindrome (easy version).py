import bisect
import sys
from collections import defaultdict
from itertools import permutations
from typing import List

input = sys.stdin.readline

def solve(n: int, s: List[int]):
    pos = defaultdict(list)
    for i, e in enumerate(s):
        pos[e].append(i)

    max_val = max(len(l) for l in pos.values())
    for a, b in permutations(pos.keys(), 2):
        pa = pos[a]
        pb = pos[b]

        pos_dict = {}
        for i in range(len(pb)):
            # pos_dict[i] = len(list(filter(lambda x: x < pb[i], pa)))
            pos_dict[i] = bisect.bisect(pa, pb[i])

        for pb_start in range(len(pb)):
            for pb_end in range(pb_start, len(pb)):
                left_len = pos_dict[pb_start]
                right_len = len(pa) - pos_dict[pb_end]
                v = (pb_end - pb_start + 1) + min(left_len, right_len) * 2
                max_val = max(max_val, v)
    return max_val


#
# assert solve(1, list(map(int, '26'.split()))) == 1
# assert solve(9, [1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
# assert solve(9, [1, 1, 1, 2, 2, 2, 1, 2, 1]) == 7
# assert solve(6, [1, 1, 1, 2, 2, 2]) == 3
# assert solve(6, [3, 1, 1, 1, 1, 3]) == 6
# assert solve(6, [3, 3, 1, 3, 1, 3]) == 5
# assert solve(5, [3, 3, 1, 1, 3]) == 4
# assert solve(5, [3, 1, 1, 3, 3]) == 4
# assert solve(11, [3, 1, 1, 3, 2, 3, 3, 3, 1, 1, 1]) == 8
# assert solve(4, [1, 3, 4, 3]) == 3
# assert solve(4, list(map(int, '4 1 4 1'.split()))) == 3
# assert solve(8, list(map(int, '1 1 2 2 3 2 1 1'.split()))) == 7
# assert solve(5, [1, 1, 3, 2, 2]) == 2
# assert solve(3, list(map(int, '1 3 3'.split()))) == 2
# assert solve(4, list(map(int, '1 10 10 1'.split()))) == 4
# assert solve(2, list(map(int, '2 1'.split()))) == 1
# assert solve(3, list(map(int, '1 1 1'.split()))) == 3
# assert solve(4, [2, 4, 3, 3]) == 2
# assert solve(4, list(map(int, '3 3 3 1'.split()))) == 3

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    r = solve(n, s)
    print(r)
