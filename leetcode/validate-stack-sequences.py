from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []
        for e in pushed:
            stack.append(e)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)


s = Solution()
assert s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
assert not s.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2])
