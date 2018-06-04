class Solution(object):
    def exist(self, board, word):
        n, m = len(board), len(board[0])

        def search(b, v, n, m, cur, w):
            if len(w) == 0:
                return True
            v[cur[0]][cur[1]] = True
            for x, y, in [(cur[0] - 1, cur[1]), (cur[0], cur[1] + 1), (cur[0] + 1, cur[1]), (cur[0], cur[1] - 1)]:
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                if board[x][y] == w[0] and v[x][y] == False and search(b, v, n, m, (x, y), w[1:]):
                    return True
            v[cur[0]][cur[1]] = False
            return False

        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and search(board, visited, n, m, (i, j), word[1:]):
                    return True
        return False
