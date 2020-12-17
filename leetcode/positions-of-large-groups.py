from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start_idx = 0
        r = []
        for i, e in enumerate(s[1:], start=1):
            if s[start_idx] != e:
                if i - start_idx >= 3:
                    r.append([start_idx, i - 1])
                start_idx = i
        if len(s) - start_idx >= 3:
            r.append([start_idx, len(s) - 1])
        return r


s = Solution()
assert s.largeGroupPositions('abbxxxxzzy') == [[3, 6]]
assert s.largeGroupPositions('abc') == []
assert s.largeGroupPositions('abcdddeeeeaabbbcd') == [[3, 5], [6, 9], [12, 14]]
