class Solution(object):
    def findLongestWord(self, s, d):
        def verify_candidate(s, w):
            i = j = 0
            n, m = len(s), len(w)
            while i < n and j < m:
                while i < n and s[i] != w[j]:
                    i += 1
                if i < n and s[i] == w[j]:
                    i += 1
                    j += 1
            return j == m

        r = ''
        for w in d:
            is_candidate = verify_candidate(s, w)
            if is_candidate:
                if len(w) > len(r):
                    r = w
                elif len(w) == len(r) and w < r:
                    r = w
        return r
