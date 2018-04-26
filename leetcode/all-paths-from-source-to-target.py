from collections import deque

class Solution:
	def allPathsSourceTarget(self, graph):
		n = len(graph)
		t = n - 1
		p = [] * n


		q = deque()
		q.append((0, [0]))
		r = []
		while len(q) > 0:
			e, local_path = q.popleft()
			if e == t:
				r.append(local_path)
				continue
			for i in graph[e]:
				new_path = local_path.copy()
				new_path.append(i)
				q.append((i, new_path))

		return r


s = Solution()
print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))