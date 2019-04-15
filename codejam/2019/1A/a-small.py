"""
## Name of Prob
Pylons

## Link
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e03

## Note
직전 방문 행, 열, 대각방향을 겹치지 않게 RxC 사이즐르 다 방문
## Input
t
r c
r c
...

## Output
IMPOSSIBLE

POSSIBLE
order of visit vertices

## Strategy

### small 전략
small 은 다 놓아보면 될 듯 함.
시작 point 몇개 두고
(R x C) 개 놓기, 시작점이 될 수 있는 것도 (R x C)

N^4 (N이 5니까 가능)
"""

_DEBUG = True
num_of_test = int(input())

grid = history = None


def possible(current_idx, r, c, pre_i=-10000, pre_j=-1000):
	global history

	if current_idx == r * c:
		return True
	for i in range(1, r + 1):
		for j in range(1, c + 1):
			if grid[i][j]:
				continue
			if i == pre_i or j == pre_j or (i - j) == (pre_i - pre_j) or (i + j) == (pre_i + pre_j):
				continue
			grid[i][j] = True
			history.append((i, j))
			if possible(current_idx + 1, r, c, i, j):
				return True
			grid[i][j] = False
			history.pop()
	return False


def solve(r, c):
	global grid
	global history
	grid = [[False] * (c + 1) for _ in range(r + 1)]
	history = []
	return possible(0, r, c)


for test_num in range(1, num_of_test + 1):
	row, col = map(int, input().split())

	solution_exists = solve(row, col)
	if solution_exists:
		print("Case #{}: {}".format(test_num, "POSSIBLE"))
		for r, c in history:
			print(r, c)
	else:
		print("Case #{}: {}".format(test_num, "IMPOSSIBLE"))
