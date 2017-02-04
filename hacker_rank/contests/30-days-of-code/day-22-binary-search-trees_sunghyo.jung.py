__author__ = 'sunghyo.jung'

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
    # Codes for submission begin
    def getHeight(self,root):
        if root is None or root.data is None:
            return 0
        return 1 + max([self.getHeight(root.left), self.getHeight(root.right)])
        #Write your code here
    # Codes for submission end

# Codes for test

T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print height
