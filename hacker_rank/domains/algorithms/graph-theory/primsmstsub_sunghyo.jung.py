import operator

n, m = map(int, raw_input().split())
g = {}
for i in range(m):
    x, y, s = map(int, raw_input().split())
    if not x in g:
        g[x] = {}
    if not y in g:
        g[y] = {}

    if not y in g[x]:
        g[x][y] = s
    else:
        g[x][y] = min([g[x][y], s])
    if not x in g[y]:
        g[y][x] = s
    else:
        g[y][x] = min([g[y][x], s])

s = [int(raw_input())]

c = 0
for i in range(n - 1):
    next_node = -1
    next_value = 1000000
    for j in s:
        if len(g[j]) == 0:
            continue

        l = sorted(g[j].items(), key=operator.itemgetter(1))
        if l[0][1] < next_value:
            next_node = l[0][0]
            next_value = l[0][1]
    for s_elem in s:
        if next_node in g[s_elem]:
            del g[s_elem][next_node]
    g[next_node] = {k: g[next_node][k] for k in filter(lambda x: not x in s, g[next_node])}

    s.append(next_node)
    c += next_value
print(c)
