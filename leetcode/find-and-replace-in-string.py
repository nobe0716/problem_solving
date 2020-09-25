from typing import List


class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        r = ''
        i = 0

        sorted_elems = sorted(zip(indexes, sources, targets))
        for start_pos, src, dst in sorted_elems:
            r += S[i:start_pos]
            tok = S[start_pos:start_pos + len(src)]
            if tok == src:
                r += dst
            else:
                r += tok
            i = start_pos + len(src)
        r += S[sorted_elems[-1][0] + len(sorted_elems[-1][1]):]
        return r


s = Solution()
assert s.findReplaceString("vmokgggqzp", [3, 5, 1], ["kg", "ggq", "mo"], ["s", "so", "bfr"]) == "vbfrssozp"
assert s.findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]) == 'eeebffff'
