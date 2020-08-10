import sys

input = sys.stdin.readline

q, x = map(int, input().split())
c = [0] * x
ans = 0

for _ in range(q):
    n = int(input())
    c[n % x] += 1
    while c[ans % x] > 0:
        c[ans % x] -= 1
        ans += 1
    print(ans)
