class ComplexNumber:
	def __init__(self, d, i):
		self.d = d
		self.i = i

	def of(s):
		d = int(s.split('+')[0])
		i = int(s.split('+')[1][:-1])
		return ComplexNumber(d, i)

	def pro(self, cn):
		d = self.d * cn.d - self.i * cn.new_number
		i = self.d * cn.new_number + self.i * cn.d
		return ComplexNumber(d, i)

	def __str__(self):
		return str(self.d) + '+' + str(self.i) + 'i'


class Solution:
	def complexNumberMultiply(self, a, b):
		"""
		:type a: str
		:type b: str
		:rtype: str
		"""
		ca = ComplexNumber.of(a)
		cb = ComplexNumber.of(b)
		return str(ca.pro(cb))
