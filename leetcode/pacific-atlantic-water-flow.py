from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        n, m = len(matrix), len(matrix[0])

        rp = [[False] * m for _ in range(n)]
        qp = set()

        ra = [[False] * m for _ in range(n)]
        qa = set()

        rp[0][0] = ra[n - 1][m - 1] = True

        for i in range(n):
            rp[i][0] = True
            qp.add((i, 0))

            ra[i][m - 1] = True
            qa.add((i, m - 1))

        for i in range(m):
            rp[0][i] = True
            qp.add((0, i))

            ra[n - 1][i] = True
            qa.add((n - 1, i))

        def bfs(mat, q):
            while q:
                nq = set()
                for x, y in q:
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m and matrix[x][y] <= matrix[nx][ny] and not mat[nx][ny]:
                            mat[nx][ny] = True
                            nq.add((nx, ny))
                q = nq

        bfs(rp, qp)
        bfs(ra, qa)

        r = []
        for i in range(n):
            for j in range(m):
                if rp[i][j] and ra[i][j]:
                    r.append([i, j])

        return r


s = Solution()
assert s.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
