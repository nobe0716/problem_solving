"""
WIP
"""

CONST_MAX_VAL = 2000
n = int(input())
a = list(map(int, input().split()))
operations = []

k = 0
idx = n - 1

while k <= n + 1 and any(a[i] >= a[i + 1] for i in range(n - 1)):
    target_value = idx * CONST_MAX_VAL
    if a[idx] >= target_value and (idx == n - 1 or a[idx] < a[idx + 1]):
        idx -= 1
        continue

    if a[idx] < target_value:
        k += 1
        d = target_value - a[idx]
        operations.append((1, idx + 1, d))
        for i in range(idx + 1):
            a[i] += d
    elif a[idx] >= a[idx + 1]:
        d = a[idx] - target_value
        k += 1
        operations.append((2, idx + 1, d))
        for i in range(idx + 1):
            a[i] %= d

if k >= n + 1:
    print(0)
else:
    print(k)
    for op in operations:
        print(op[0], op[1], op[2])
