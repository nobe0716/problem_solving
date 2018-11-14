l, r = list(map(int, input().split()))
print('YES')
i = l
for _ in range((r - l) // 2 + 1):
    print(i, i + 1)
    i += 2
