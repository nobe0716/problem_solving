"""
## Name of Prob
753. Cracking the Safe

## Link
https://leetcode.com/problems/cracking-the-safe/

## Note

return minimum len string which has every possible combination of k ^ n(with zero padding) as own sub-sequence

## Input
n, k

1 <= n <= 4
1 <= k <= 10
k ^ n <= 4096

## Output

## Strategy

For l-len str, there exists (l - n + 1) n-len-substrs

k ^ n = (l - n + 1)
l = k ^ n + n - 1

So I guess that minimum-len must be larger or equals than (k ^ n + n - 1), and it is right for given two examples :$

n = 1, k = 10 => 10 + 1 - 1 = 10 is right cus one of answer is 0123456789

since k ^ n up to 4096, len may be bound to 4096 + 4 - 1 = 4099.

In optimal str, m(1 <= m <= n) length of str must appear k ** (n - m)
So if we construct str using that restriction, it may works

use backtracking and cut if there is no hope to retrieve solution
under restriction that "n-len substr must appear once"

"""
import sys
from typing import List, Set

sys.setrecursionlimit(10000)


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        def stringfy(l: List[int]) -> str:
            return ''.join(map(str, l))

        def dfs(l: int, current_list: List[int], collected_ones: Set[str]) -> str:
            if l == (k ** n + n - 1):
                return ''.join(map(str, current_list))
            for i in range(k):
                current_list.append(i)
                new_member = stringfy(current_list[len(current_list) - n:]) if l >= n - 1 else None

                if new_member and new_member in collected_ones:
                    current_list.pop()
                    continue

                if new_member:
                    collected_ones.add(new_member)
                res = dfs(l + 1, current_list, collected_ones)
                if res is not None:
                    return res

                current_list.pop()
                collected_ones.discard(new_member)
            return None

        return dfs(0, [], set())


s = Solution()
print(s.crackSafe(1, 2))
print(s.crackSafe(2, 2))
print(s.crackSafe(3, 10))  # TLE
