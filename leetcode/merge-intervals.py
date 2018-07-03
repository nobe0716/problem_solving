# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
	def merge(self, intervals):
		l = sorted(intervals, key=lambda interval: interval.start)
		cur = None
		r = []
		for interval in l:
			if cur is None:
				cur = Interval(interval.start, interval.end)
			elif cur.end < interval.start:
				r.append(cur)
				cur = Interval(interval.start, interval.end)
			else:
				cur.end = max(cur.end, interval.end)
		if cur is not None:
			r.append(cur)
		return r