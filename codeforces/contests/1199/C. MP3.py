from collections import Counter

n, I = map(int, input().split())
a = list(map(int, input().split()))
c = Counter(a)
sorted_keys = sorted(c.keys())

acc_counts = [0] * (len(c) + 1)
sorted_keys_len = len(sorted_keys)
for i in range(1, sorted_keys_len + 1):
    acc_counts[i] = acc_counts[i - 1] + c[sorted_keys[i - 1]]
# acc_counts[i] = sum(a[0:i])
# acc_counts[y] - acc_counts[x] = sum(a[0:y]) - sum(a[0:x]) = sum(a[x:y])

variations = 2 ** (8 * I // n)

if variations >= sorted_keys_len:
    print(0)
else:
    min_v = float('inf')
    for i in range(1, sorted_keys_len + 1 - variations):
        x, y = i, i + variations
        v = acc_counts[y] - acc_counts[x]
        min_v = min(min_v, n - v)
    print(min_v)
