from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(list)
for i in range(n):
    d[a[i]].append(i)
sum_of_a = sum(a)

r = []
for i in range(n):
    rest_sum_of_a = sum_of_a - a[i]
    if rest_sum_of_a % 2 == 1 or (rest_sum_of_a // 2) not in d:
        continue
    target_list = d[rest_sum_of_a // 2]
    if len(target_list) >= 2 or target_list[0] != i:
        r.append(i + 1)

print(len(r))
print(' '.join(map(str, r)))
