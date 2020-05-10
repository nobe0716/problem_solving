_MODER = 10 ** 9 + 7

t, k = map(int, input().split())

abs = []
min_a, max_b = float('inf'), -float('inf')
for _ in range(t):
    a, b = map(int, input().split())
    min_a = min(min_a, a)
    max_b = max(max_b, b)
    abs.append((a, b))

t = [0] * (max_b + 1)
s = [0] * (max_b + 1)

for i in range(k):
    t[i] = 1

for i in range(k, max_b + 1):
    t[i] = (t[i - 1] + t[i - k]) % _MODER

for i in range(min_a, max_b + 1):
    s[i] = (s[i - 1] + t[i]) % _MODER

for a, b in abs:
    r = s[b] - s[a - 1]
    print(r if r >= 0 else (_MODER + r))
