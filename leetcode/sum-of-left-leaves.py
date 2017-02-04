
class Solution(object):
    def sumOfLeftLeaves(self, root):
        queue = [root]
        sum = 0
        while len(queue) > 0:
            node = queue.pop(0)
            if node is None:
                continue
            sum = (node.left.val if node.left is not None else 0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return sum


            1
        2       3
    4       5