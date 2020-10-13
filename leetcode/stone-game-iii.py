from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)
        suffix_sum = [0] * n
        suffix_sum[-1] = stoneValue[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = stoneValue[i] + suffix_sum[i + 1]

        alice = [0] * (n + 1)
        bob = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            alice[i] = suffix_sum[i] - min(bob[i + 1:i + 4])
            bob[i] = suffix_sum[i] - min(alice[i + 1:i + 4])

        max_alice = alice[0]
        max_bob = suffix_sum[0] - alice[0]
        if max_alice == max_bob:
            return 'Tie'
        return 'Alice' if max_alice > max_bob else 'Bob'


s = Solution()
assert s.stoneGameIII([1, 2, 3, 7]) == 'Bob'
assert s.stoneGameIII([1, 2, 3, -9]) == 'Alice'
assert s.stoneGameIII([1, 2, 3, 6]) == 'Tie'
assert s.stoneGameIII([-1, -2, -3]) == 'Tie'
