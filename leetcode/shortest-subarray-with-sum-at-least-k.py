from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        res, cur = float('inf'), 0
        q = deque([(0, 0)])
        for i, e in enumerate(A, start=1):
            cur += e
            while q and cur - q[0][1] >= K:
                res = min(res, i - q.popleft()[0])
            while q and cur <= q[-1][1]:
                q.pop()
            q.append((i, cur))
        return res if res != float('inf') else -1


s = Solution()

assert s.shortestSubarray([27, 20, 79, 87, -36, 78, 76, 72, 50, -26], 453) == 9
assert s.shortestSubarray([2, 3, -1, 6], 6) == 1
assert s.shortestSubarray([2, -1, 3, -2, 4], 5) == 3
assert s.shortestSubarray([-34, 37, 51, 3, -12, -50, 51, 100, -47, 99, 34, 14, -13, 89, 31, -14, -44, 23, -38, 6], 151) == 2
assert s.shortestSubarray([2, -1, 3, 2, 3], 6) == 3
assert s.shortestSubarray([2, -1, 2, 2], 4) == 2
assert s.shortestSubarray([1, 93, 5, 54, 47, -7, 23, -28, -9, 43], 193) == 4
assert s.shortestSubarray([2, -1, 2, 3], 3) == 1
assert s.shortestSubarray([-28, 81, -20, 28, -29], 89) == 3
assert s.shortestSubarray([2, -1, 2], 3) == 3
assert s.shortestSubarray([1, 2], 4) == -1
assert s.shortestSubarray([56, -21, 56, 35, -9], 61) == 2
assert s.shortestSubarray([1], 1) == 1
assert s.shortestSubarray([58701, 23101, 6562, 60667, 20458, -14545, 74421, 54590, 84780, 63295, 33238, -10143, -35830, -9881, 67268, 90746, 9220, -15611, 23957, 29506, -33103, -14322, 19079, -34950, -38551, 51786, -48668, -17133, 5163, 15122, 5463, 74527, 1111, -3281, 73035, -28736, 32910, 17414, 4080, -42435, 66106, 48271, 69638, 14500, 37084, -9978, 85748, -43017, 75337, -27963, -34333, -25360, 82454, 87290, 87019, 84272, 17540, 60178, 51154, 19646, 54249, -3863, 38665, 13101, 59494, 37172, -16950, -30560, -11334, 27620, 73388, 34019, -35695, 98999, 79086, -28003, 87339, 2448, 66248, 81817, 73620, 28714, -46807, 51901, -23618, -29498, 35427, 11159, 59803, 95266, 20307, -3756, 67993, -31414, 11468, -28307, 45126, 77892, 77226, 79433], 1677903) == 48
assert s.shortestSubarray(
    [-49914, -12426, -5186, 70636, -25230, 71719, 90865, -25838, 87988, 44944, -31171, -9539, -18668, -16799, 802, 12192, 71687, -22054, -33194, 67975, -46508, 95593, 52415, -23572, 18245, 34385, -18305, 3349, 21403, 92653, 2597, 5573, 99636, 28790, 28184, 5524, -30978, 13236, -829, 19458, -44034, 10808, 17197, 53301, -9512, 54704, 3896, 68958, 55937, -42208, 55831, 61437, 43108, -7713, 71722, 14715, -22091, 5555, 62545, 4480, -34749, -36968, 96064, 42491, 25270, 99998, -43873, 75212, 93923, -18801, 95238, 88265, -14835, -46249, 66837, -29596, 90566, 32159, 58118, -35383, 12354, 91203, 58472, 22909, 21620, -2113, 27080, 35674, -45367, 29767, 4157, 24475, -43348, -47608, -15407, -5378, 60187, 26210, -38533, 48496, 50526, 97819, 43815, -49106, -10727, 17860, 15885, 79713, 86535, 14218, 84271, 19657, 6295, -47146, 29794, 91599, -20032, -22164, 16799, 24086, 78542, 48258, 69127, -20043, 60309, 17502, 99910, 68640, 67616, -7979, -41240, 55544, 3027, -23308, 85859, 33054, 32536, -40949,
     5712, 12317, 22468, 90870, 22308, 14800, -287, 62913, -580, 79031, 7515, 61095, -28931, 82973, 58185, -36839, 33472, 64011, 94597, 71154, 94935, 25907, 74492, -1308, 88318, 39634, -31847, -7888, 26374, 54748, 84470, 54312, 36294, -31614, 1311, -25330, 48564, 63977, 1760, 40859, 715, -49656, 32512, -28909, -14475, -33104, 22544, -30756, -9719, 90357, 74164, 94641, 50135, 6875, 50675, 73998, -17559, -35592, -36108, 22285, -21966, -38227], 855005) == 19