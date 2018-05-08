class Solution(object):
    def minimumLengthEncoding(self, words):
        words = sorted(words, key=lambda x: len(x), reverse=True)
        s = ''
        for e in words:
            if (e + '#') not in s:
                s += e + '#'
        return len(s)