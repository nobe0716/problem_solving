from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        roots = [-1] * n

        for i in range(n):
            parent = i
            lc, rc = leftChild[i], rightChild[i]

            while roots[parent] > 0:
                parent = roots[parent]

            if lc >= 0:
                if roots[lc] >= 0:
                    return False
                roots[lc] = parent
            if rc >= 0:
                if roots[rc] >= 0:
                    return False
                roots[rc] = parent

        return len(list(filter(lambda x: x == -1, roots))) == 1


s = Solution()
assert s.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1])
assert not s.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1])
assert not s.validateBinaryTreeNodes(n=2, leftChild=[1, 0], rightChild=[-1, -1])
assert not s.validateBinaryTreeNodes(n=6, leftChild=[1, -1, -1, 4, -1, -1], rightChild=[2, -1, -1, 5, -1, -1])
