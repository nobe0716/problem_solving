import heapq
from typing import List

MODULO = 10 ** 9 + 7


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eff_spd = sorted(zip(efficiency, speed), reverse=True)

        spd_heap = []
        max_perf = 0
        sum_of_spd = 0

        for i in range(k):
            eff, spd = eff_spd[i]
            heapq.heappush(spd_heap, spd)

            sum_of_spd += spd
            cur_perf = sum_of_spd * eff
            if max_perf < cur_perf:
                max_perf = cur_perf

        for i in range(k, n):
            eff, spd = eff_spd[i]

            if spd < spd_heap[0]:
                continue

            heapq.heappush(spd_heap, spd)
            sum_of_spd = sum_of_spd + spd - spd_heap[0]
            heapq.heappop(spd_heap)
            cur_perf = sum_of_spd * eff
            if max_perf < cur_perf:
                max_perf = cur_perf
        return max_perf % MODULO


s = Solution()
assert s.maxPerformance(3, [2, 8, 2], [2, 7, 1], 2) == 56
assert s.maxPerformance(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=2) == 60
assert s.maxPerformance(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=3) == 68
assert s.maxPerformance(n=6, speed=[2, 10, 3, 1, 5, 8], efficiency=[5, 4, 3, 9, 7, 2], k=4) == 72
