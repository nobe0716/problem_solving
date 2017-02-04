class Solution(object):
    def pacificAtlantic(self, matrix):
        if len(matrix) == 0:
            return []
        r = []
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        n = len(matrix)
        m = len(matrix[0])
        is_pacific = [[False] * m for _ in range(n)]
        is_atlantic = [[False] * m for _ in range(n)]

        q = []
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            q.append([i, 0])
            visited[i][0] = True
        for i in range(m):
            q.append([0, i])
            visited[0][i] = True

        while len(q) > 0:
            p = q.pop(0)
            is_pacific[p[0]][p[1]] = True
            for i in range(4):
                if not(0 <= p[0] + dx[i] < n and 0 <= p[1] + dy[i] < m):
                    continue
                if visited[p[0] + dx[i]][p[1] + dy[i]]:
                    continue
                if matrix[p[0] + dx[i]][p[1] + dy[i]] >= matrix[p[0]][p[1]]:
                    visited[p[0] + dx[i]][p[1] + dy[i]] = True
                    q.append([p[0] + dx[i], p[1] + dy[i]])

        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            q.append([i, m - 1])
            visited[i][m - 1] = True
        for i in range(m):
            q.append([n - 1, i])
            visited[n - 1][i] = True
        while len(q) > 0:
            p = q.pop(0)
            is_atlantic[p[0]][p[1]] = True
            for i in range(4):
                if not(0 <= p[0] + dx[i] < n and 0 <= p[1] + dy[i] < m):
                    continue
                if visited[p[0] + dx[i]][p[1] + dy[i]]:
                    continue
                if matrix[p[0] + dx[i]][p[1] + dy[i]] >= matrix[p[0]][p[1]]:
                    visited[p[0] + dx[i]][p[1] + dy[i]] = True
                    q.append([p[0] + dx[i], p[1] + dy[i]])
        for i in range(n):
            for j in range(m):
                if is_pacific[i][j] and is_atlantic[i][j]:
                    r.append([i, j])
        return r


s = Solution()
print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))