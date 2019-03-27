SORT_FUNCTION = lambda query: query[1] * n + query[0]

num_of_t = int(input())

_DEBUG = False


def remain_times(tt, q):
	count = 0
	for i in range(q[0], q[1] + 1):
		if tt[i] == 0:
			count += 1
	return count


def reserve(tt, q):
	if _DEBUG:
		print("Reserve! ", q)
	for i in range(q[0], q[1] + 1):
		tt[i] = 1


for t in range(1, num_of_t + 1):
	n, q = map(int, input().split())
	queries = []
	for _ in range(q):
		l, r = map(int, input().split())
		queries.append([l, r])

	# heapq.heapify()
	queries = list(sorted(queries, key=SORT_FUNCTION))
	# queries = enu
	if _DEBUG:
		print(queries)

	at_least_count = float('inf')
	time_table = [0] * (n + 1)

	s = []
	order_list = []
	for i, query in enumerate(queries):
		while len(s) > 0:
			last_idx, last_elem = s[-1]
			remain_time_last_elem = remain_times(time_table, last_elem)
			remain_time_new_query = remain_times(time_table, query)
			if remain_time_last_elem < remain_time_new_query:
				s.pop()
				order_list.append(last_idx)
				reserve(time_table, last_elem)
				at_least_count = min(at_least_count, remain_time_last_elem)
			else:
				break
		s.append((i, query))

	for i, query in s[::-1]:
		remain_time = remain_times(time_table, query)
		reserve(time_table, query)
		at_least_count = min(at_least_count, remain_time)

	print("Case #{}: {}".format(t, at_least_count))
