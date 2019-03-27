from collections import defaultdict

_DEBUG = False
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

num_of_t = int(input())


def display_distance_table(distance_table):
	if not _DEBUG:
		return

	print("#########DISTANCE_TABLE###########")
	for i in range(1, row_size + 1):
		for j in range(1, col_size + 1):
			print('{:4}'.format(distance_table[(i, j)]), end='')
		print()


def find_maximum_distance(g, r_size, c_size):
	# global orig_q, distance_table, visited, i, j, pos, maximum_cost, maximum_cost_pos, new_q, r, c, d, new_pos
	orig_q = []
	distance_table = defaultdict(lambda: 999)
	visited = set()
	for i in range(1, r_size + 1):
		for j in range(1, c_size + 1):
			if g[i][j] == 1:
				pos = (i, j)
				orig_q.append(pos)
				distance_table[pos] = 0
				visited.add(pos)
	maximum_cost = 0
	maximum_cost_pos = []
	while len(orig_q) > 0:
		new_q = []
		for r, c in orig_q:
			for d in range(4):
				new_pos = r + dr[d], c + dc[d]
				if not (1 <= new_pos[0] <= r_size and 1 <= new_pos[1] <= c_size):
					continue
				if new_pos in visited:
					continue
				visited.add(new_pos)
				new_q.append(new_pos)
				distance_table[new_pos] = distance_table[(r, c)] + 1

				if distance_table[new_pos] > maximum_cost:
					maximum_cost = distance_table[new_pos]
					maximum_cost_pos = [new_pos]
				elif distance_table[new_pos] == maximum_cost:
					maximum_cost_pos.append(new_pos)
		orig_q = new_q
	return maximum_cost, maximum_cost_pos, distance_table


for t in range(1, num_of_t + 1):
	row_size, col_size = map(int, input().split())
	grid = list()
	grid.append([0] * (col_size + 2))

	for _ in range(row_size):
		grid.append([0] + list(map(int, list(input()))) + [0])
	grid.append([0] * (col_size + 2))

	max_cost, max_cost_pos, dist_table = find_maximum_distance(grid, row_size, col_size)
	# print(maximum_cost_pos)
	display_distance_table(dist_table)

	if len(max_cost_pos) == 0:
		print("Case #{}: 0".format(t))
		continue

	result_cost = float('inf')
	for i in range(1, row_size + 1):
		for j in range(1, col_size + 1):
			if grid[i][j] == 1:
				continue
			candidate_pos = (i, j)
			# if dist_table[candidate_pos] > result_cost:
			# 	continue
			if dist_table[candidate_pos] >= max_cost // 2:
				grid[i][j] = 1
				tmp_cost, tmp_cost_pos, tmp_dist_table = find_maximum_distance(grid, row_size, col_size)
				result_cost = min(result_cost, tmp_cost)
				grid[i][j] = 0
	print("Case #{}: {}".format(t, result_cost))
