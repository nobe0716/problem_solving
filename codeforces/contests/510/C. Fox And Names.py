import string
from collections import defaultdict


def solve(n, s):
    g = defaultdict(set)
    edges = []
    for i in range(n - 1):
        condition = None
        for ca, cb in zip(s[i], s[i + 1]):
            if ca == cb:
                continue
            condition = ca, cb
            break
        if condition is None:
            if len(s[i]) > len(s[i + 1]):
                return None
            continue
        parent, child = condition
        edges.append((parent, child))
        g[parent].add(child)

    visited = set()

    def gen_topology(e):
        if e in visited:
            return
        visited.add(e)
        if e in g:
            for next in g[e]:
                if next in visited:
                    continue
                gen_topology(next)
        stack.append(e)

    stack = []
    for e in g.keys():
        if e in visited:
            continue
        gen_topology(e)

    weight = {}
    for i, e in enumerate(stack[::-1]):
        weight[e] = i

    for parent, child in edges:
        if weight[parent] > weight[child]:
            return None

    r = stack[::-1]
    for e in string.ascii_lowercase:
        if e not in r:
            r.append(e)
    return r


n = int(input())
s = [input() for _ in range(n)]

r = solve(n, s)
if not r:
    print('Impossible')
else:
    print(''.join(r))
