n = int(input())
t = [0] * (n + 1)
f = [0] * (n + 1)

t[3] = 2
f[:4] = [0, 1, 2, 6]
_MODER = 10 ** 9 + 7
for i in range(4, n + 1):
    f[i] = f[i - 1] * i % _MODER
    t[i] = (2 * t[i - 1] + (i - 2) * f[i - 1]) % _MODER
print(t[n])
