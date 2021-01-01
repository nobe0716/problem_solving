from typing import List


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        limit = len(tree)
        if not tree or limit <= 2:
            return limit
        one_idx = 0
        two_idx = [0]
        r = 0
        for i in range(1, limit):
            if tree[i] != tree[two_idx[0]] and tree[i] != tree[two_idx[-1]]:
                if len(two_idx) == 0:
                    two_idx.append(i)
                else:
                    r = max(r, i - two_idx[0])
                    two_idx = [one_idx, i]
            if tree[i] != tree[one_idx]:
                one_idx = i

        return max(r, limit - two_idx[0])


s = Solution()
assert s.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
