import heapq
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        fuel = startFuel
        gas_heap = []
        refills = 0
        for pos, gas in stations:
            if fuel >= target:
                break

            while gas_heap and fuel < pos:
                fuel -= heapq.heappop(gas_heap)
                refills += 1

            if not gas_heap and fuel < pos:
                break
            heapq.heappush(gas_heap, -gas)

        while gas_heap and fuel < target:
            fuel -= heapq.heappop(gas_heap)
            refills += 1

        return refills if fuel >= target else -1


s = Solution()
assert s.minRefuelStops(1, 1, []) == 0
assert s.minRefuelStops(target=100, startFuel=1, stations=[[10, 100]]) == -1
assert s.minRefuelStops(target=100, startFuel=10, stations=[[10, 60], [20, 30], [30, 30], [60, 40]]) == 2
assert s.minRefuelStops(100, 25, [[25, 25], [50, 25], [75, 25]]) == 3
