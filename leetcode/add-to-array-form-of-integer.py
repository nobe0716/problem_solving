from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:

        idx = -1
        carry = 0
        while K > 0 or carry > 0:
            if -idx > len(A):
                A = [0] + A
            v = A[idx] + K % 10 + carry
            A[idx], carry, K = v % 10, v // 10, K // 10
            idx -= 1
        return A


s = Solution()
assert s.addToArrayForm(A=[2, 7, 4], K=181) == [4, 5, 5]
assert s.addToArrayForm(A=[0], K=34) == [3, 4]
assert s.addToArrayForm(A=[1, 2, 0, 0], K=34) == [1, 2, 3, 4]
assert s.addToArrayForm(A=[2, 1, 5], K=806) == [1, 0, 2, 1]
assert s.addToArrayForm(A=[9, 9, 9, 9, 9, 9, 9, 9, 9, 9], K=1) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
