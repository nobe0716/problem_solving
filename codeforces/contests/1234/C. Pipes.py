# https://codeforces.com/problemset/problem/1234/C
def solve(n, pipes) -> bool:
    row = 0
    for col in range(0, n):
        if col == n - 1:
            if row == 1:
                return pipes[row][col] < 3
            else:
                return pipes[0][col] >= 3 and pipes[1][col] >= 3
        if pipes[row][col] < 3:
            continue
        if pipes[(row + 1) % 2][col] < 3:
            return False
        row = (row + 1) % 2

    return False


assert solve(3, [[5, 3, 6], [3, 4, 5]])
assert solve(2, [[1, 2], [3, 4]]) is False

for _ in range(int(input().strip())):
    n = int(input().strip())
    pipes = [list(map(int, list(input().strip()))), list(map(int, list(input().strip())))]
    ans = solve(n, pipes)
    if ans:
        print('YES')
    else:
        print('NO')
