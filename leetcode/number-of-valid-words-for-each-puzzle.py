from collections import defaultdict
from typing import List


class Tri:
    def __init__(self):
        self.cnt = 0
        self.next = defaultdict(lambda: Tri())


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        roots = defaultdict(lambda: Tri())
        for word in words:
            word = sorted(set(word))
            if len(word) > 7:
                continue

            for i in range(len(word)):
                k, rest = word[i], word[:i] + word[i + 1:]
                node = roots[k]
                for e in rest:
                    node = node.next[e]
                node.cnt += 1

        ans = []
        for puzzle in puzzles:
            k, rest = puzzle[0], set(puzzle[1:])
            node = roots[k]

            v = 0
            q = [node]
            while q:
                nq = []
                for e in q:
                    v += e.cnt

                    for n in e.next.keys():
                        if n in rest:
                            nq.append(e.next[n])
                q = nq
            ans.append(v)

        return ans


s = Solution()
ans = s.findNumOfValidWords(
    ["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
    ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"])
print(ans)
