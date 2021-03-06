from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        n, m = len(board), len(board[0])
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

        def back(x, y, idx, v):
            if idx == len(word):
                return True

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if not (0 <= nx < n and 0 <= ny < m) or board[nx][ny] != word[idx] or (nx, ny) in v:
                    continue
                v.add((nx, ny))
                if back(nx, ny, idx + 1, v):
                    return True
                v.discard((nx, ny))
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] != word[0]:
                    continue
                if back(i, j, 1, {(i, j)}):
                    return True
        return False


s = Solution()
assert s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
assert not s.exist(
    [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]],
    "ABCB")
