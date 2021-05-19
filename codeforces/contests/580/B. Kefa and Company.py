# https://codeforces.com/contest/580/problem/B
n, d = map(int, input().split())
friends = []
for _ in range(n):
    mi, si = map(int, input().split())
    friends.append((mi, si))

friends.sort()

res = 0
local_sum = hi = 0

for lo in range(0, n):
    while hi < n and friends[hi][0] - friends[lo][0] < d:
        local_sum += friends[hi][1]
        hi += 1
    res = max(res, local_sum)
    local_sum -= friends[lo][1]
print(res)
