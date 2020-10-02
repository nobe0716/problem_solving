from typing import List

next_nodes = {str(x): (str((x + 10 - 1) % 10), str((x + 1) % 10)) for x in range(10)}


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        distances = {x: float('inf') for x in deadends}

        def gen(node: str):
            for i in range(4):
                next_node = node[:i] + next_nodes[node[i]][0] + node[i + 1:]
                if next_node not in distances:
                    yield next_node
                next_node = node[:i] + next_nodes[node[i]][1] + node[i + 1:]
                if next_node not in distances:
                    yield next_node

        loop_count = 0
        q = {'0000'}
        while q and target not in q:
            nq = set()
            loop_count += 1
            for node in q:
                for next_node in gen(node):
                    distances[next_node] = loop_count
                    nq.add(next_node)
            q = nq
        return loop_count if target in q else -1


s = Solution()
assert s.openLock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6
assert s.openLock(deadends=["8888"], target="0009") == 1

assert s.openLock(deadends=["8888"], target="0009") == 1
assert s.openLock(deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], target="8888") == -1
