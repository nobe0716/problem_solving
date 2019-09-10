n, d, e = [int(input()) for _ in range(3)]
DOLLAR_BILLS = [1, 2, 5, 10, 20, 50, 100]
EURO_BILLS = [5, 10, 20, 50, 100, 200]
min_rest = float('inf')
for i in range(0, n // e + 1):
    if i % 5 != 0:
        continue
    rest = (n - (i * e)) % d
    min_rest = min(min_rest, rest)
print(min_rest)
