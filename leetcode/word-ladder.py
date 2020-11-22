import string
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = {beginWord}
        word_set = set(wordList)
        d = 1
        visited = set()
        while q and endWord not in q:
            nq = set()
            d += 1
            for e in q:
                for i in range(len(e)):
                    for c in string.ascii_lowercase:
                        ne = e[:i] + c + e[i + 1:]
                        if ne in word_set and ne not in visited:
                            visited.add(e)
                            nq.add(ne)

            q = nq
        return d if endWord in q else 0


s = Solution()
assert s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
