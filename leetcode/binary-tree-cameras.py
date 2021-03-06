# Definition for a binary tree node.
import sys
from collections import deque
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        _BIG_NUM = 10 ** 9
        sys.setrecursionlimit(1001)

        def label_node(node: TreeNode):
            if not node:
                return
            node.val = v[0]
            node_dict[v[0]] = node
            v[0] += 1
            label_node(node.left)
            label_node(node.right)

        v = [1]
        node_dict = {}
        label_node(root)

        @lru_cache(None)
        def dp_all(val: int, parent_on: bool) -> int:  # regardless current light on/off
            return min(dp(val, parent_on, False), dp(val, parent_on, True))

        @lru_cache(None)
        def dp(val: int, parent_on: bool, current_on: bool) -> int:
            node = node_dict[val]
            if parent_on or current_on:
                res = 1 if current_on else 0
                if node.left:
                    res += dp_all(node.left.val, current_on)
                if node.right:
                    res += dp_all(node.right.val, current_on)
                return res
            # parent_off && current_off ; one of child should be on
            if node.left and node.right:
                return min(dp(node.left.val, current_on, True) + dp_all(node.right.val, current_on),
                           dp_all(node.left.val, current_on) + dp(node.right.val, current_on, True))
            elif node.left:
                return dp(node.left.val, current_on, True)
            elif node.right:
                return dp(node.right.val, current_on, True)
            else:
                return _BIG_NUM

        if not root:
            return 0
        return dp_all(root.val, False)


s = Solution()


def test(inputs):
    if not inputs:
        return None

    root = TreeNode()
    q = deque([root])
    for i in range(1, len(inputs), 2):
        l, r = inputs[i], inputs[i + 1]
        node = q.popleft()
        if l == 0:
            node.left = TreeNode()
            q.append(node.left)
        if r == 0:
            node.right = TreeNode()
            q.append(node.right)
    return s.minCameraCover(root)


# [0,null,0,null,0,0,0]
assert test([0, None, 0, None, 0, 0, 0]) == 2
assert test([0, 0, None, 0, 0]) == 1
assert test([0, 0, None, 0, None, 0, None, None, 0]) == 2
assert test([0]) == 1
