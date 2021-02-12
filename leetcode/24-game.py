from functools import lru_cache
from itertools import permutations
from typing import List

_EPSILON = 10 ** -10


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        def get_comb(a: int, b: int) -> List[float]:
            return [a + b, a - b, a * b, a / b]

        for arr in permutations(nums):
            @lru_cache(None)
            def dfs(i: int, j: int, k: float) -> bool:  # i; next idx, v; current value
                if j == i + 1:
                    return arr[i] == k
                elif j == i + 2:
                    # 1 + 1
                    for v in (arr[i] + arr[i + 1], arr[i] - arr[i + 1], arr[i] * arr[i + 1], arr[i] / arr[i + 1]):
                        if abs(k - v) < _EPSILON:
                            return True
                    return False

                # take one from first
                # a[i] + dfs[i+1:j] == k or a[i] - dfs[i+1:j] == k or a[i] * dfs[i+1:j] == k or a[i] / dfs[i+1:j] == k
                if dfs(i + 1, j, k - arr[i]) or dfs(i + 1, j, arr[i] - k) or dfs(i + 1, j, k / arr[i]) or dfs(i + 1, j, arr[i] / k):
                    return True
                # take one from last
                # dfs[i:j-1] + a[j-1] == k or dfs[i:j-1] - a[j-1] == k or dfs[i:j-1] * a[j-1] == k or dfs[i:j-1] / a[j-1] == k
                if dfs(i, j - 1, k - arr[j - 1]) or dfs(i, j - 1, k + arr[j - 1]) or dfs(i, j - 1, k / arr[j - 1]) or dfs(i, j - 1, k * arr[j - 1]):
                    return True

                # take two from first
                if i + 2 < j:
                    for e in get_comb(arr[i], arr[i + 1]):
                        if dfs(i + 2, j, k - e) or dfs(i + 2, j, e - k):
                            return True
                        if k > 0 and e > 0 and dfs(i + 2, j, k / e):
                            return True
                        if k > 0 and e > 0 and dfs(i + 2, j, e / k):
                            return True
                return False

            if dfs(0, 4, 24.0):
                return True
            dfs.cache_clear()
        return False


s = Solution()
assert not s.judgePoint24([1, 2, 1, 2])
assert s.judgePoint24([1, 9, 1, 2])
assert s.judgePoint24([3, 3, 7, 7])
assert s.judgePoint24([1, 3, 4, 6])
assert s.judgePoint24([4, 1, 8, 7])
assert s.judgePoint24([1, 3, 4, 6])
