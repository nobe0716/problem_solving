class Solution:
	def isValidBST(self, root):
		def search(root):
			if root is None:
				return [True, None, None]
			lr = search(root.left)
			rr = search(root.right)
			if not lr[0] or not rr[0]:
				return [False, None, None]
			if lr[2] is not None and lr[2] >= root.val:
				return [False, None, None]
			if rr[1] is not None and rr[1] <= root.val:
				return [False, None, None]
			minimum_val = root.val if lr[1] is None else lr[1]
			maximum_Val = root.val if rr[2] is None else rr[2]
			return [True, minimum_val, maximum_Val]
		return search(root)[0]