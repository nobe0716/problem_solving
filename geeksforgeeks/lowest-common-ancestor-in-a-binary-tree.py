# User function Template for python3

'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''


# If LCA exist, return reference to it. If
# If both n1 and n2 are not present, 
# rturn None. Else if left subtree contains any 
#  of them return pointer to left.
def lca(root, n1, n2):
    def find(node, n1, n2):
        if node is None:
            return None, [False, False]
        lnode, lr = find(node.left, n1, n2)
        rnode, rr = find(node.right, n1, n2)

        if lnode:
            return lnode, lr
        elif rnode:
            return rnode, rr
        res = [node.data == n1 or lr[0] or rr[0], node.data == n2 or lr[1] or rr[1]]
        if all(res):
            return node, res
        return None, res

    return find(root, n1, n2)[0]