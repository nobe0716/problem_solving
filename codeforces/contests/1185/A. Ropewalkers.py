a, b, c, d = map(int, input().split())
a, b, c = sorted([a, b, c])

if b - a >= d and c - b >= d:
    print(0)
elif c - a >= 2 * d:  # move b only
    if b - a < d:
        print(d - (b - a))
    else:
        print(d - (c - b))
else:  # must move a or b
    print(max(d - (b - a), 0) + max(d - (c - b), 0))
