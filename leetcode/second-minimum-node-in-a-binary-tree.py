class Solution(object):
    def findSecondMinimumValue(self, root):
        def find_minimum(root, bound):
            if root.left == None:
                return root.val if root.val > bound else float('inf')
            lv, rv = find_minimum(root.left, bound), find_minimum(root.right, bound)
            return lv if lv < rv else rv
        v  = find_minimum(root, root.val)
        return -1 if v == float('inf') else v