from collections import defaultdict
from operator import itemgetter
from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topo_sort(elems: List[int], in_edges, out_edges):
            order = []
            stack = [e for e in elems if not in_edges[e]]
            while stack:
                s = stack.pop()
                order.append(s)

                for e in out_edges[s]:
                    in_edges[e].remove(s)
                    if not in_edges[e]:
                        stack.append(e)
            return order if len(order) == len(elems) else []

        in_edges_group = defaultdict(set)
        out_edges_group = defaultdict(set)

        in_edges_node = defaultdict(set)
        out_edges_node = defaultdict(set)

        new_group = m
        for i in range(n):
            if group[i] == -1:
                group[i] = new_group
                new_group += 1

        for i in range(n):
            for e in beforeItems[i]:
                out_edges_node[e].add(i)
                in_edges_node[i].add(e)

                if group[i] != group[e]:
                    out_edges_group[group[e]].add(group[i])
                    in_edges_group[group[i]].add(group[e])

        topo_g = topo_sort(list(range(new_group)), in_edges_group, out_edges_group)
        topo_n = topo_sort(list(range(n)), in_edges_node, out_edges_node)
        if not topo_g or not topo_n:
            return []

        group_rank = {}
        for i in range(new_group):
            group_rank[topo_g[i]] = i

        node_rank = {}
        for i in range(n):
            node_rank[topo_n[i]] = i

        v = []
        for i, g in enumerate(group):
            v.append((group_rank[g], node_rank[i], i))

        v.sort()
        return list(map(itemgetter(2), v))


s = Solution()
print(s.sortItems(5,
                  5,
                  [2, 0, -1, 3, 0],
                  [[2, 1, 3], [2, 4], [], [], []]))
# print(s.sortItems(8,
#                   2,
#                   [-1, -1, 1, 0, 0, 1, 0, -1],
#                   [[], [6], [5], [6], [3, 6], [], [], []]))
