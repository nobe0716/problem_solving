from collections import defaultdict, deque

n, m = map(int, input().split())
has_cat = [0] + list(map(int, input().split()))
is_leaf = [False] * (n + 1)
visitable = [0] * (n + 1)
# compose graph
graph = defaultdict(set)
for _ in range(n - 1):
    xi, yi = map(int, input().split())
    graph[xi].add(yi)
    graph[yi].add(xi)

# convert to tree
q = deque([(-1, 1)])

while q:
    parent, node = q.popleft()

    if parent in graph[node]:
        graph[node].remove(parent)

    if len(graph[node]) == 0:  # is_leaf
        is_leaf[node] = True
        continue

    for child in graph[node]:
        q.append((node, child))

# proc
q = deque([(1, 0)])

while q:
    node, cats = q.popleft()
    cats = (cats + 1) if has_cat[node] else 0

    if cats > m:
        continue

    if is_leaf[node]:
        visitable[node] = 1
    else:
        for child in graph[node]:
            q.append((child, cats))

res = sum(visitable)
print(res)
