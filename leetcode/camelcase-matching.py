import string
from collections import defaultdict
from typing import List

Trie = lambda: [defaultdict(Trie), False]


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        head = Trie()

        for s in queries:
            node = head
            for c in s:
                node = node[0][c]
            node[1] = s

        lowercase_set = set(string.ascii_lowercase)

        set_matched_queries = set()

        def traverse(node: Trie, pattern: str):
            trie, val = node
            if pattern == '':
                if val:
                    set_matched_queries.add(val)

            for k in trie.keys():
                if len(pattern) > 0 and k == pattern[0]:
                    traverse(trie[k], pattern[1:])
                if k in lowercase_set:
                    traverse(trie[k], pattern)

        traverse(head, pattern)
        return [x in set_matched_queries for x in queries]


s = Solution()
assert s.camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FB") == \
       [True, False, True, True, False]
assert s.camelMatch(queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern="FoBa") == \
       [True, False, True, False, False]
