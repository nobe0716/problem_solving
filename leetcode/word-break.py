class Solution:
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		l = len(s)
		if l == 0:
			return True
		t = [False] * (l + 1)
		t[0] = True

		wd = {w: len(w) for w in wordDict}

		for i in range(l):
			if not t[i]:
				continue
			for k in wd:
				if i + wd[k] > l:
					continue
				if k == s[i:i + wd[k]]:
					t[i + wd[k]] = True
		return t[l]
