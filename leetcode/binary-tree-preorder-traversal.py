class Solution(object):
    def preorderTraversal(self, root):
        def travel(r, v):
            if r is None:
                return
            v.append(r.val)
            travel(r.left, v)
            travel(r.right, v)
        v = []
        travel(root, v)
        return v
