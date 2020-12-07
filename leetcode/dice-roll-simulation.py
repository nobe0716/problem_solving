from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        _MODER = 10 ** 9 + 7

        maximum_dup_allowed = max(rollMax)
        t = [[[0] * (maximum_dup_allowed + 1) for _ in range(6)] for _ in range(n + 1)]

        for i in range(6):
            t[1][i][1] = 1

        for roll_no in range(1, n):
            for dice_num in range(6):
                for k in range(1, rollMax[dice_num] + 1):
                    if not t[roll_no][dice_num][k]:
                        continue
                    t[roll_no][dice_num][k] %= _MODER

                    for next_dice_num in range(6):
                        if next_dice_num != dice_num:
                            t[roll_no + 1][next_dice_num][1] += t[roll_no][dice_num][k]
                        elif k < rollMax[dice_num]:
                            t[roll_no + 1][dice_num][k + 1] += t[roll_no][dice_num][k]
        r = 0
        for dice_num in range(6):
            for k in range(rollMax[dice_num] + 1):
                r = (r + t[n][dice_num][k]) % _MODER
        return r


s = Solution()
assert s.dieSimulator(n=2, rollMax=[1, 1, 1, 1, 1, 1]) == 30
assert s.dieSimulator(n=2, rollMax=[1, 1, 2, 2, 2, 3]) == 34
assert s.dieSimulator(n=3, rollMax=[1, 1, 1, 2, 2, 3]) == 181
assert s.dieSimulator(n=5000, rollMax=[15, 15, 15, 15, 15, 15]) == 549903798
