class Solution(object):
    def diameterOfBinaryTree(self, root):
        def lp(root):  # # of node, diameter
            if root is None:
                return (0, 0)
            elif root.left is None and root.right is None:
                return (1, 0)
            l = lp(root.left)
            r = lp(root.right)

            n = max(l[0], r[0]) + 1
            v = [l[0] + r[0], l[1], r[1]]
            return (n, max(v))

        if root is None:
            return 0
        r = lp(root)
        return max(r[0] - 1, r[1])