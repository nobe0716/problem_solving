class Solution(object):
    def findCircleNum(self, M):
        n_circles = 0
        n_members = len(M)
        if n_members == 0:
            return 0
        visited = [False] * n_members
        for i in range(n_members):
            if visited[i]:
                continue
            visited[i] = True
            q = [i]
            while len(q) > 0:
                e = q.pop(0)
                for j in range(n_members):
                    if visited[j]:
                        continue
                    if M[e][j] == 0:
                        continue
                    visited[j] = True
                    q.append(j)
            n_circles += 1
        return n_circles
