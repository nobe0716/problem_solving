from collections import Counter

class Solution(object):

    def to_key(self, c):
        key = ""
        for k in sorted(c.keys()):
            key += k + "_" + str(c[k]) + "/"
        return key

    def groupAnagrams(self, strs):
        groups = {}
        for s in strs:
            c = Counter(s)
            k = self.to_key(c)
            if k in groups:
                groups[k].append(s)
            else:
                groups[k] = [s]
        return groups.values()