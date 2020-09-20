from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        v = 0
        r = []
        j = 0
        for i, e in enumerate(arr):
            v += arr[i]
            while j < i and v > target:
                v -= arr[j]
                j += 1
            if v == target:
                # if len(r) == 0:
                window_size = i - j + 1
                # r.append((window_size, j, i))
                if not r:
                    r.append((window_size, j, i))
                elif window_size != r[-1][0] or r[-1][2] < j:
                    r.append((window_size, j, i))

        if len(r) < 2:
            return -1

        r.sort()
        min_res = float('inf')
        for i in range(len(r) - 1):
            a = r[i]
            if a[0] + r[i + 1][0] >= min_res:
                break
            for j in range(i + 1, len(r)):
                b = r[j]
                if a[2] < b[1] or b[2] < a[1]:
                    min_res = min(min_res, a[0] + b[0])

        return min_res if min_res != float('inf') else -1


s = Solution()
assert s.minSumOfLengths([2,2,4,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 20) == 23
assert s.minSumOfLengths([1, 6, 1], 7) == -1
assert s.minSumOfLengths([1, 1, 1, 2, 2, 2, 4, 4], 6) == 6
assert s.minSumOfLengths([2, 1, 3, 3, 2, 3, 1], 6) == 5
assert s.minSumOfLengths(arr=[3, 2, 2, 4, 3], target=3) == 2
assert s.minSumOfLengths(arr=[7, 3, 4, 7], target=7) == 2
assert s.minSumOfLengths(arr=[4, 3, 2, 6, 2, 3, 4], target=6) == -1
assert s.minSumOfLengths(arr=[5, 5, 4, 4, 5], target=3) == -1
assert s.minSumOfLengths(arr=[3, 1, 1, 1, 5, 1, 2, 1], target=3) == 3