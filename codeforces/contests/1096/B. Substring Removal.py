n = int(input())
s = input()
i, j = 0, n - 1
while i < n and s[i] == s[0]:
    i += 1
while j >= 0 and s[j] == s[-1]:
    j -= 1

r = 0
if i == n:
    r = n * (n - 1) // 2 + n
else:
    if s[0] == s[-1]:
        r = (i + 1) * (n - j)
    else:
        r = i + n - j

print(r % 998244353)
