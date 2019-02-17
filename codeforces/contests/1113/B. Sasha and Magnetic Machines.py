n = int(input())
a = list(sorted(list(map(int, input().split())), reverse=True))
original_sum = sum(a)
minimum_sum = original_sum
min_v = a[-1]
for i in range(n - 1):
    for j in range(2, a[i] - 1):
        if a[i] % j == 0:
            current_sum = original_sum - a[i] - min_v + a[i] // j + min_v * j
            minimum_sum = min(minimum_sum, current_sum)
print(minimum_sum)
