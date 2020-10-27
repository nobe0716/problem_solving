from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        l = len(A)
        al, am, tl, tm = ([0] * l for _ in range(4))
        if L > M:
            L, M = M, L

        al[L - 1] = sum(A[:L])
        am[M - 1] = sum(A[:M])

        for _ in range(L, l):
            al[_] = al[_ - 1] + A[_] - A[_ - L]
        for _ in range(M, l):
            am[_] = am[_ - 1] + A[_] - A[_ - M]

        for _ in range(L - 1, l):
            tl[_] = max(al[_], tl[_ - 1])
        for _ in range(M - 1, l):
            tm[_] = max(am[_], tm[_ - 1])

        r = 0
        for _ in range(L + M - 1, l):
            r = max(r, al[_] + tm[_ - L], am[_] + tl[_ - M])
        return r


s = Solution()
assert s.maxSumTwoNoOverlap([1, 0, 3], 1, 2) == 4
assert s.maxSumTwoNoOverlap([1, 0, 1], 1, 1) == 2
assert s.maxSumTwoNoOverlap(A=[2, 1, 5, 6, 0, 9, 5, 0, 3, 8], L=4, M=3) == 31
assert s.maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2) == 20
assert s.maxSumTwoNoOverlap(A=[3, 8, 1, 3, 2, 1, 8, 9, 0], L=3, M=2) == 29
