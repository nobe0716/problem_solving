__author__ = 'sunghyo.jung'

tree = {}
n, m = map(int, raw_input().split())
for i in range(m):
    child, parent = map(int, raw_input().split())
    if not parent in tree:
        tree[parent] = []
    tree[parent].append(child)

def cut_tree(node):
    if not node in tree:
        return 0, 1
    subtree_cnt = 0
    child_cnt = 0
    for child in tree[node]:
        sc, cc = cut_tree(child)
        subtree_cnt += sc
        if cc % 2 == 0:
            subtree_cnt += 1
        else:
            child_cnt += cc
    return subtree_cnt, child_cnt + 1

sc, cc = cut_tree(1)

print(sc)

