class Solution(object):
    def findRepeatedDnaSequences(self, s):
        def encode(t):
            c = 0
            d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
            for e in t:
                c = c * 4 + d[e]
            return c

        def decode(c):
            d = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
            t = ''
            for i in range(10):
                t = d[c % 4] + t
                c /= 4
            return t

        d = {}
        for i in range(len(s) - 9):
            v = encode(s[i:i + 10])
            if v not in d:
                d[v] = 0
            d[v] += 1
        # print(d)
        return list(sorted(decode(k) for k in d if d[k] > 1))