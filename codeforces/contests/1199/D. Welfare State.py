n = int(input())
a = [int(x) for x in input().split()]
q = int(input())

ans = [None] * n
events = [input() for _ in range(q)]

max_val = 0
for i in range(q - 1, -1, -1):
    event = events[i]
    if event[0] == '1':  # we have a receipt that the balance of the p-th person becomes equal to x.
        event = event[2:].split()
        p = int(event[0]) - 1
        if ans[p] is None:
            ans[p] = max(max_val, int(event[1]))
    else:
        max_val = max(max_val, int(event[2:]))

for i in range(n):
    if ans[i] is None:
        ans[i] = max(a[i], max_val)
print(' '.join(map(str, ans)))
