import sys
from typing import List, Set

sys.setrecursionlimit(10000)


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        def back(cur: List[int], visited: Set[str]) -> str:
            if len(cur) == k ** n + n - 1:
                return ''.join(map(str, cur))
            for i in range(k):
                cur.append(i)

                if len(cur) < n:  # simply extends
                    res = back(cur, visited)
                    if res:
                        return res
                else:
                    ns = ''.join(map(str, cur[-n:]))
                    if ns not in visited:
                        visited.add(ns)
                        res = back(cur, visited)
                        if res:
                            return res
                        visited.discard(ns)
                cur.pop()
            return None

        return back([], set())


s = Solution()
print(s.crackSafe(1, 2))
print(s.crackSafe(2, 2))
print(s.crackSafe(3, 10))  # TLE
