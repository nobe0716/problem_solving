import math
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def find_divisors(n):
            divisors = []
            for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    divisors.append(i)
            return divisors

        minimum_abs_diff = float('inf')
        r = None
        divisor = find_divisors(num + 1)[-1]
        r = [divisor, (num + 1) // divisor]

        divisor = find_divisors(num + 2)[-1]
        if (num + 2) // divisor - divisor < r[1] - r[0]:
            r = [divisor, (num + 2) // divisor]
        return r


s = Solution()
assert s.closestDivisors(999) == [25, 40]
assert s.closestDivisors(8) == [3, 3]
assert s.closestDivisors(123) == [5, 25]
