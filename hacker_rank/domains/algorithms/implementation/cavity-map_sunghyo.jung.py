__author__ = 'sunghyo.jung'
n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
    grid_t = str(raw_input().strip())
    grid.append(grid_t)

pos = []
for i in xrange(1, n - 1):
    for j in xrange(1, n - 1):
        if int(grid[i][j]) - 1 >= max(map(int, [grid[i - 1][j], grid[i + 1][j], grid[i][j - 1], grid[i][j + 1]])):
            pos.append([i, j])
for i, j in pos:
    grid[i] = grid[i][:j] + 'X' + grid[i][j + 1:]
for row in grid:
    print str(row).replace('[', '').replace(']', '').replace(',', '')

