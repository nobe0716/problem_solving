import re

class Solution(object):
	def myAtoi(self, str):
		m = re.search(r'(^\s*[-+]?[\d]+)', str)
		if m is None:
			return 0
		v = int(m.group(1))
		if v > 0x7FFFFFFF:
			return 0x7FFFFFFF
		elif v < -0x80000000:
			return -0x80000000
		else:
			return v