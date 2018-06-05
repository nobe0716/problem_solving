class Solution(object):
    def minSwap(self, A, B):
        l = len(A)
        if l == 0:
            return 0

        v_swap = [1] + [float('inf')] * (l - 1)
        v_no_swap = [0] + [float('inf')] * (l - 1)
        for i in range(1, l):
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                v_swap[i] = min(v_swap[i], v_no_swap[i - 1] + 1)
                v_no_swap[i] = min(v_no_swap[i], v_swap[i - 1])
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                v_swap[i] = min(v_swap[i], v_swap[i - 1] + 1)
                v_no_swap[i] = min(v_no_swap[i], v_no_swap[i - 1])
        return min(v_swap[l - 1], v_no_swap[l - 1])
