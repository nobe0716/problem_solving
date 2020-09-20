import functools


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        @functools.lru_cache(None)
        def solve(n, m):
            if n == m:
                return 1
            if n == 1:
                return m
            if m == 1:
                return n

            candidates = []
            for i in range(1, m):
                candidates.append(solve(n, i) + solve(n, m - i))
            for i in range(1, n):
                candidates.append(solve(i, m) + solve(n - i, m))

            for k in range(1, n):
                for i in range(1, n - k):
                    for j in range(1, m - k):
                        candidates.append(
                            solve(i, j + k) + solve(i + k, m - j - k) + solve(n - i - k, m - j) + solve(n - i, j) + 1
                        )
            return min(candidates)

        return solve(n, m)


s = Solution()
assert s.tilingRectangle(11, 13) == 6
assert s.tilingRectangle(10, 9) == 6
