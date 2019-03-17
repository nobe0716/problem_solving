n = int(input())
t = list(map(int, input().split()))
# v = [[0, 0]]
first = 0
tokens = []
for i in range(1, n):
    if t[first] != t[i]:
        token = [t[first], i - first]
        tokens.append(token)
        first = i
tokens.append([t[first], n - first])
# print(tokens)

r = 0
for i in range(len(tokens) - 1):
    if tokens[i][0] != tokens[i + 1][0]:
        r = max(r, min(tokens[i][1], tokens[i + 1][1]))
print(r * 2)
