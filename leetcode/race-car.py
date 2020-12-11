import heapq


class Solution:
    def racecar(self, target: int) -> int:
        # depth, diff(= |target - pos|), pos, speed
        h = [(0, target, 0, 1)]
        t = {0: 0}

        while h and target not in t:
            depth, diff, pos, speed = heapq.heappop(h)
            new_pos = pos + speed
            new_speed = speed * 2

            t[new_pos] = depth + 1
            heapq.heappush(h, (depth + 1, abs(new_pos - target), new_pos, new_speed))

            if (new_pos - target) * speed > 0:
                heapq.heappush(h, (depth + 1, diff, pos, 1 if speed < 0 else -1))
        return t[target]


s = Solution()
assert s.racecar(2) == 4
assert s.racecar(3) == 2
assert s.racecar(6) == 5
assert s.racecar(20) == 12
assert s.racecar(10000) == 45

# 20
#
# 1 2 4 8 -1  1  2  4  8 -1 -2  1  2
# 0 1 3 7 15 15 16 18 22 22 21 19 20
# 0 1 2 3  4  5  6  7  8  9 10 11 12
