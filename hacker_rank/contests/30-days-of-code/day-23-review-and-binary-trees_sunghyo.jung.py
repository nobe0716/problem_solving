__author__ = 'sunghyo.jung'
import sys
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def levelOrder(self,root):
        # Write your code here
        q = []
        q.append(root)
        while len(q) > 0:
            elem = q.pop(0)
            print elem.data,
            if elem.left is not None:
                q.append(elem.left)
            if elem.right is not None:
                q.append(elem.right)
        print ''

T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)