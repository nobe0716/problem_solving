from collections import defaultdict


class Solution(object):
    def longestWord(self, words):
        def helper(head, cur):
            r = ''
            if head[1]:
                r = cur
            else:
                return ''

            for k in head[0]:
                candidate = helper(head[0][k], cur + k)
                if len(candidate) > len(r) or (len(candidate) == len(r) and candidate < r):
                    r = candidate
            return r

        TrieNode = lambda: [defaultdict(TrieNode), False]
        head = TrieNode()

        for w in words:
            node = head
            for c in w:
                node = node[0][c]
            node[1] = True
        head[1] = True
        return helper(head, '')
