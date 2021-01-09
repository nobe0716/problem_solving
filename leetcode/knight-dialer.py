from collections import defaultdict


class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        next_steps = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }

        base = {_: 1 for _ in range(10)}
        for _ in range(n - 1):
            next = defaultdict(int)

            for i in range(10):
                for j in next_steps[i]:
                    next[j] += base[i]

            for i in range(1, 10):
                next[i] %= MOD
            base = next
        return sum(base.values()) % MOD


s = Solution()
assert s.knightDialer(2) == 20
assert s.knightDialer(1) == 10
assert s.knightDialer(3) == 46
assert s.knightDialer(4) == 104
assert s.knightDialer(3131) == 136006598
