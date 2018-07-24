class Solution(object):
	def letterCombinations(self, digits):
		if len(digits) == 0:
			return []
		d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

		v = self.letterCombinations(digits[1:])
		v = [""] if len(v) == 0 else v
		r = []
		for e in d[digits[0]]:
			r += list(map(lambda y: e + y, v))
		return r