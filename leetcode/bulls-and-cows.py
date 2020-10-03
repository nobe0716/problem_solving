from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(1 if s == g else 0 for s, g in zip(secret, guess))
        cs, cg = Counter(secret), Counter(guess)
        cows = sum(min(cs[k], v) for k, v in cg.items()) - bulls
        return '{}A{}B'.format(bulls, cows)


s = Solution()
assert s.getHint('1807', '7810') == '1A3B'
assert s.getHint('1123', '0111') == '1A1B'
