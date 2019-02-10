n, m, k = map(int, input().split())
a = [-10 ** 9 - 1] + list(map(int, input().split()))
v = sorted(enumerate(a), key=lambda x: x[1], reverse=True)[:m * k]
v = list(sorted(v))
# print(v)
print(sum(map(lambda x: x[1], v)))
for i in range(m, m * k, m):
    # print(v[i])
    print(v[i][0] - 1, end=' ')
print()
