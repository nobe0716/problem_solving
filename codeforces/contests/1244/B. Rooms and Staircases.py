def solve(n, s):
	is_stairs = [s[x] == '1' for x in range(n)]
	if not any(is_stairs):
		return n
	if is_stairs[0] or is_stairs[-1]:
		return n * 2
	else:
		min_idx = max_idx = None
		for i in range(n):
			if not is_stairs[i]:
				continue
			if not min_idx:
				min_idx = i
			max_idx = i

		return max(max_idx + 1, n - min_idx) * 2


for _ in range(int(input())):
	n = int(input())
	s = input()
	r = solve(n, s)
	print(r)
