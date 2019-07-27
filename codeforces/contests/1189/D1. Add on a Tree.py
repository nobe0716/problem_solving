from collections import defaultdict

g = defaultdict(set)
n = int(input())

for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].add(v)
    g[v].add(u)


def solve(n, g):
    for i in range(1, n + 1):
        if len(g[i]) == 1 or len(g[i]) >= 3:
            continue
        else:
            return False
    return True


solution = solve(n, g)
print('YES' if solution else 'NO')