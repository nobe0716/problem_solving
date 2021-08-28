# https://codeforces.com/contest/1437/problem/D

def solve(n, a):
    if n == 1:
        return 0
    height = 1
    parent_count = 1
    node_count = 1
    last_node = a[1]
    for e in a[2:]:
        if e < last_node:
            parent_count -= 1
        if parent_count == 0:
            parent_count, node_count = node_count, 0
            height += 1
        last_node = e
        node_count += 1
    return height


assert solve(5, [1, 5, 4, 3, 2]) == 4
assert solve(5, [1, 2, 5, 4, 3, ]) == 2

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    r = solve(n, a)
    print(r)
