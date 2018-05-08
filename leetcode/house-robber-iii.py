class Solution:
    def rob(self, root):
        def search(r):
            if r is None:
                return [0, 0]
            lv = search(r.left)
            rv = search(r.right)

            return [r.val + lv[1] + rv[1], max(lv) + max(rv)]

        return max(search(root))