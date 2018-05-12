class Solution:
	def isBipartite(self, graph):
		def validate(i, graph, sa, sb):
			if i == len(graph):
				return True
			ac = len(list(filter(lambda x: x in sa, graph[i])))
			bc = len(list(filter(lambda x: x in sb, graph[i])))
			if ac > 0 and bc > 0:
				return False
			elif ac > 0: # i should be belong to set b
				sb.add(i)
				return validate(i + 1, graph, sa, sb)
			elif bc > 0: # i should be belong to set a
				sa.add(i)
				return validate(i + 1, graph, sa, sb)
			else:
				sa.add(i)
				if validate(i + 1, graph, sa, sb):
					return True
				sa.remove(i)
				sb.add(i)
				return validate(i + 1, graph, sa, sb)
		return validate(0, graph, set(), set())
