import sys
sys.setrecursionlimit(100005)

N,l = map(int,raw_input().split())

g = {}
for i in xrange(l):
    a, b = map(int,raw_input().split())

    if not a in g:
        g[a] = []
    if not b in g:
        g[b] = []
    g[a].append(b)
    g[b].append(a)

visited = set()
def count_node(node):
    if node in visited:
        return 0
    if node not in g:
        return 1
    visited.add(node)
    sum = 1
    for next in g[node]:
        sum += count_node(next)
    return sum

pool = []
for i in xrange(N):
    cn = count_node(i)
    if cn > 0:
        pool.append(cn)

#print(pool)
result = (N * (N - 1)) / 2
for m in pool:
    result -= (m * (m - 1)) / 2
# Compute the final result using the inputs from above

print result

