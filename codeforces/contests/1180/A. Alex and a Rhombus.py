n = int(input())
t = [0] * (n + 1)
t[1] = 1
for i in range(2, n + 1):
    t[i] = t[i - 1] + (i - 1) * 4
# print(t)
print(t[n])
