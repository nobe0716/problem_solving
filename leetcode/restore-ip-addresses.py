class Solution(object):
	def restoreIpAddresses(self, s):
		def back(s, c, r):
			if len(s) == 0 and len(c) == 4:
				r.append(".".join(c))
				return
			if len(c) > 4:
				return
			#print(s, c, r)
			for i in range(1, min(4, len(s) + 1)):
				v = s[:i]
				if 0 <= int(v) <= 255 and (v == '0' or v[0] != '0'):
					c.append(s[:i])
					back(s[i:], c, r)
					c.pop()
		r = []
		back(s, [], r)
		return r