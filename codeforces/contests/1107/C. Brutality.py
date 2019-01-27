n, k = map(int, input().split())
a = list(map(int, input().split()))
s = input()

r = 0
i = 0
dup_count = 0
while i < n:
    j = i + 1
    while j < n and s[i] == s[j]:
        j += 1
    if j - i <= k:
        r += sum(a[i:j])
    else:
        r += sum(sorted(a[i:j], reverse=True)[:k])
    i = j
print(r)
