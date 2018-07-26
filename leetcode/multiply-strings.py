class Solution:
	def multiply(self, num1, num2):
		if num1 == '0' or num2 == '0':
			return '0'
		num1 = num1[::-1]
		num2 = num2[::-1]

		r = [0 for _ in range(len(num1) + len(num2))]
		for idx, i in enumerate(num1):
			for jdx, j in enumerate(num2):
				v = int(i) * int(j)
				#print(i, j)
				r[idx + jdx] += v % 10
				r[idx + jdx + 1] += (v // 10 + r[idx + jdx] // 10)
				r[idx + jdx] %= 10

				#print(r)
		r.reverse()
		while len(r) > 0 and r[0] == 0:
			r = r[1:]
		return ''.join(map(str, r))