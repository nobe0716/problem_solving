# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

	def serialize(self, root):
		if root is None:
			return '()'
		else:
			return '(' + str(root.val) + '/' + self.serialize(root.left) + '|' + self.serialize(root.right) + ')'


	def deserialize(self, data):
		if data == '()':
			return None

		val_idx = None
		left_idx = None
		paren_count = 0
		for i in range(len(data)):
			if data[i] == '(':
				paren_count += 1
			elif data[i] == ')':
				paren_count -= 1
			elif paren_count != 1: # str of child nodes
				continue
			if data[i] == '/':
				val_idx = i
			elif data[i] == '|':
				left_idx = i

		val = int(data[1:val_idx])
		left_str = data[val_idx + 1:left_idx]
		right_str = data[left_idx + 1:-1]
		root = TreeNode(val)
		root.left = self.deserialize(left_str)
		root.right = self.deserialize(right_str)
		return root





# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))