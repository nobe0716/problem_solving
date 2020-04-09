class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def reduce(i, j, i_skip=0, j_skip=0):
            if i >= 0 and S[i] == '#':
                return reduce(i - 1, j, i_skip + 1, j_skip)
            if j >= 0 and T[j] == '#':
                return reduce(i, j - 1, i_skip, j_skip + 1)
            if i >= 0 and i_skip > 0:
                return reduce(i - 1, j, i_skip - 1, j_skip)
            if j >= 0 and j_skip > 0:
                return reduce(i, j - 1, i_skip, j_skip - 1)
            if i >= 0 and j >= 0 and S[i] == T[j]:
                return reduce(i - 1, j - 1)
            return i < 0 and j < 0

        return reduce(len(S) - 1, len(T) - 1)

s = Solution()
assert (s.backspaceCompare("xywrrmp", "xywrrmu#p"))
# assert (s.backspaceCompare("a##c", "#a#c"))
# assert (s.backspaceCompare("ab##", "c#d#"))
