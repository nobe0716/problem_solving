from collections import defaultdict
from typing import List


def is_predecessor(w1, w2):
    l = len(w1)
    if l + 1 != len(w2):
        return False
    i = j = 0
    while i < l and w1[i] == w2[j]:
        i += 1
        j += 1
    j += 1
    while i < l and w1[i] == w2[j]:
        i += 1
        j += 1
    return i == l and j == l + 1


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        g = defaultdict(set)

        l = len(words)
        q = set(range(l))
        nq = set()
        for i in range(l):
            for j in range(l):
                if i == j:
                    continue
                if is_predecessor(words[i], words[j]):
                    g[i].add(j)
                    q.discard(j)

        maximum_seq = defaultdict(int)
        d = 1
        while q:
            nq = set()
            for i in q:
                maximum_seq[i] = d
                for n in g[i]:
                    nq.add(n)

            d += 1
            q = nq
        return max(maximum_seq.values())


s = Solution()
assert s.longestStrChain(words=["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) == 5
assert s.longestStrChain(words=["a", "b", "ba", "bca", "bda", "bdca"]) == 4
