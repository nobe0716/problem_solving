# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        def helper(node, level, r):
            if node is None:
                return None
            if len(r) < level:
                r.append([0, 0])
            v, c = r[level - 1]
            v += node.val
            c += 1
            r[level - 1] = [v, c]
            helper(node.left, level + 1, r)
            helper(node.right, level + 1, r)

        res = []
        helper(root, 1, res)
        print(res)
        return list(map(lambda x: 1.0 * x[0] / x[1], res))
