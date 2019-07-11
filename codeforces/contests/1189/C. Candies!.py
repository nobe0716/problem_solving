n = int(input())
s = [0] + list(map(int, input().split()))
q = int(input())
t = [0] * (n + 1)

t[1] = s[1]
for i in range(2, n + 1):
    t[i] = t[i - 1] + s[i]


def solve(n, s, l, r):
    return (t[r] - t[l - 1]) // 10


for _ in range(q):
    l, r = map(int, input().split())
    print(solve(n, s, l, r))
