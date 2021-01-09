# Definition for a Node.


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        old_nodes = {}
        stack = [node]
        while stack:
            v = stack.pop()
            old_nodes[v.val] = v
            for e in v.neighbors:
                if e.val not in old_nodes:
                    old_nodes[e.val] = e
                    stack.append(e)

        n = len(old_nodes)
        new_nodes = {_: Node(_) for _ in range(1, n + 1)}

        for i in range(1, n + 1):
            if not old_nodes[i]:
                continue

            old_node = old_nodes[i]
            new_node = new_nodes[i]
            for neighbor in old_node.neighbors:
                new_node.neighbors.append(new_nodes[neighbor.val])

        return new_nodes[1]
