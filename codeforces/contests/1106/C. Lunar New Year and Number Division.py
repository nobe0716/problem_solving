n = int(input())
a = list(sorted(map(int, input().split())))
print(sum((a[i] + a[n - i - 1]) ** 2 for i in range(n // 2)))
