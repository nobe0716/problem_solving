class Solution(object):
    def reverseWords(self, s):
        r = []
        for e in s.strip().split():
            r.append(e)
        return ' '.join(reversed(r))
