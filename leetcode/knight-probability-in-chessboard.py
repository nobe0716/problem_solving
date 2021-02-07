class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        def next_pos(x, y):
            dx = [-1, -2, -2, -1, 1, 2, 2, 1]
            dy = [-2, -1, 1, 2, 2, 1, -1, -2]
            next = []
            for d in range(8):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    next.append((nx, ny))
            return next

        t = [[0] * N for _ in range(N)]
        t[r][c] = 1.0
        while K > 0:
            # print(K)
            nt = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    base = t[i][j]
                    if not base:
                        continue
                    next = next_pos(i, j)
                    for x, y in next:
                        nt[x][y] += base / 8
                        # print(i, j, x, y, base / 8)

            K -= 1
            t = nt
        r = sum(sum(t[i]) for i in range(N))
        # print(r)
        return r


s = Solution()
assert s.knightProbability(3, 2, 0, 0) == 0.0625
