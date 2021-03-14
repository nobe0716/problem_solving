from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        arr = [sum(nums[:k])]
        for i in range(k, len(nums)):
            arr.append(arr[-1] - nums[i - k] + nums[i])

        t = [[0] * len(arr) for _ in range(4)]
        h = [[0] * len(arr) for _ in range(4)]

        t[1][0] = arr[0]
        h[1][0] = 0
        for i in range(1, len(arr)):
            if arr[i] > t[1][i - 1]:
                t[1][i] = arr[i]
                h[1][i] = i
            else:
                t[1][i] = t[1][i - 1]
                h[1][i] = h[1][i - 1]

        for i in range(2, 4):
            t[i][(i - 1) * k] = t[i - 1][(i - 2) * k] + arr[(i - 1) * k]
            h[i][(i - 1) * k] = (i - 1) * k
            for j in range(k * (i - 1) + 1, len(arr)):
                if arr[j] + t[i - 1][j - k] > t[i][j - 1]:
                    t[i][j] = arr[j] + t[i - 1][j - k]
                    h[i][j] = j
                else:
                    t[i][j] = t[i][j - 1]
                    h[i][j] = h[i][j - 1]

        r = [h[3][len(arr) - 1]]
        r = [h[2][r[-1] - k]] + r
        r = [h[1][r[-2] - k]] + r
        return r


s = Solution()
assert s.maxSumOfThreeSubarrays([1, 2, 1, 2, 1, 2, 1, 2, 1], 2) == [0, 2, 4]
assert s.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2) == [0, 3, 5]
