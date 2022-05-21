from typing import List


class Node:
    def __init__(self, fc):
        self.idx = fc[0]
        self.v = set(fc[1])
        self.child = []

    def try_insert(self, node):
        if self.v.intersection(node.v) != node.v:
            return False
        if any(e.try_insert(node) for e in self.child):
            return True
        self.child.append(node)
        return True


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sorted_list = sorted(enumerate(favoriteCompanies), key=lambda x: len(x[1]), reverse=True)

        max_len = len(sorted_list[0][1])
        roots = [Node(sorted_list[0])]
        for i, e in sorted_list[1:]:
            new_node = Node((i, e))
            if len(e) != max_len and any(e.try_insert(new_node) for e in roots):
                continue
            roots.append(new_node)
        return sorted(e.idx for e in roots)

s = Solution()
ans = s.peopleIndexes(
    [["leetcode", "google", "facebook"], ["google", "microsoft"], ["google", "facebook"], ["google"], ["amazon"]])
assert ans == [0, 1, 4]
