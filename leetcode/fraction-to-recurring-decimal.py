class Solution:
	def fractionToDecimal(self, numerator, denominator):
		if numerator % denominator == 0:
			return str(numerator // denominator)
		s = -1 if ((numerator < 0) ^ (denominator < 0)) else 1
		numerator, denominator = abs(numerator), abs(denominator)
		w, r = divmod(numerator, denominator)
		d = {}
		v = ('-' if s < 0 else '') + str(w)
		#print(s, w)
		if r > 0:
			v += '.'
		d[r] = len(v)
		while r > 0:
			#print(v)
			w, r = divmod(r * 10, denominator)
			v += str(w)
			if r in d:
				return v[:d[r]] + '(' + v[d[r]:] + ')'
			d[r] = len(v)
		return v