n = int(input())
a = list(map(int, input().split()))
sum_of_all_elements = sum(a)
tot_even_sum = tot_odd_sum = 0

for i in range(0, n):
    if i % 2 == 0:
        tot_even_sum += a[i]
    else:
        tot_odd_sum += a[i]

cur_odd_sum = cur_even_sum = 0

r = 0
for i in range(n):
    if i % 2 == 0:
        if cur_odd_sum + tot_even_sum - cur_even_sum - a[i] == cur_even_sum + tot_odd_sum - cur_odd_sum:
            # print(i + 1)
            r += 1
        cur_even_sum += a[i]
    else:
        if cur_odd_sum + tot_even_sum - cur_even_sum == cur_even_sum + tot_odd_sum - cur_odd_sum - a[i]:
            # print(i + 1)
            r += 1
        cur_odd_sum += a[i]
print(r)
