n = int(input())
trees = []
for _ in range(n):
    x, h = map(int, input().split())
    trees.append([x, h])

res = min(2, n)  # this is fishing, tree number can be 1 -_-a
for i in range(1, n - 1):
    x, h = trees[i]
    if x - h > trees[i - 1][0]:
        res += 1
    elif x + h < trees[i + 1][0]:
        res += 1
        trees[i][0] = x + h

print(res)
