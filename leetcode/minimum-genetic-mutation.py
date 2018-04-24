from collections import deque


class Solution(object):
    def minMutation(self, start, end, bank):
        # d = [float('inf')] * (len(bank) + 1)
        d = {b: float('inf') for b in bank}
        d[start] = 0
        c = "ACGT"
        q = deque()
        q.append(start)

        if end not in bank:
            return -1

        while len(q) > 0:
            node = q.popleft()
            for i in range(8):
                # original_i = node[i]
                for ch in c:
                    new_node = node[:i] + ch + node[i + 1:]
                    if new_node == end:
                        return d[node] + 1
                    if new_node in d and d[node] + 1 < d[new_node]:
                        d[new_node] = d[node] + 1
                        q.append(new_node)
        return -1

s = Solution()
print(s.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
print(s.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))
print(s.minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]))
