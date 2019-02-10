from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
indexes = defaultdict(list)

begin_index = 0
for i in range(1, n):
    if a[i] == a[begin_index]:
        continue
    # different color => [begin_index:i] will be same color
    # index_ = a[begin_index]
    indexes[a[begin_index]].append([begin_index, i])
    begin_index = i
indexes[a[begin_index]].append([begin_index, n])
# print(indexes)

total_interval_count = 0
t = [0] * n
for color, intervals in indexes.items():
    interval_count = len(intervals)
    total_interval_count += interval_count
    for i in range(interval_count - 1):
        from_interval, to_interval = intervals[i], intervals[i + 1]
        for j in range(from_interval[1], to_interval[0]):
            t[j] += 1

max_pos = max(enumerate(t), key=lambda x: x[1])
# print(t)
# print(max_pos)
# print(total_interval_count)
print(total_interval_count - max_pos[1] - 1)
