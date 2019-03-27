num_of_t = int(input())
for t in range(1, num_of_t + 1):
	n, p = map(int, input().split())
	s = [0] + list(sorted(map(int, input().split())))
	sequence_sum_table = [0] * (n + 1)
	# print(s)
	r = float('inf')
	sequence_sum_table[p] = sum(s[1:p + 1])
	for i in range(p + 1, n + 1):
		sequence_sum_table[i] = sequence_sum_table[i - 1] - s[i - p] + s[i]

	for i in range(p, n + 1):
		r = min(r, s[i] * p - sequence_sum_table[i])
	print("Case #{}: {}".format(t, r))
