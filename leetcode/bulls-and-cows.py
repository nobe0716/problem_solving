from collections import Counter


class Solution:
	def getHint(self, secret: str, guess: str) -> str:
		cs, cg = Counter(secret), Counter(guess)
		bulls = cows = 0
		for k, v in cs.items():
			cows += min(v, cg[k])

		for i in range(len(secret)):
			if secret[i] == guess[i]:
				bulls += 1
				cows -= 1
		return '{}A{}B'.format(bulls, cows)


s = Solution()
print(s.getHint('1807', '7810'))
print(s.getHint('1123', '0111'))
