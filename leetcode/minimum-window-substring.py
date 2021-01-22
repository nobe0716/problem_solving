from collections import Counter
from typing import Optional


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lo, hi = len(t), len(s)
        res = None

        keys = set(t)
        len_s = len(s)
        counter_target = Counter(t)

        def validate(k: int) -> Optional[str]:
            def can_cover(c1: Counter, c2: Counter) -> bool:
                return all(c1[_] >= c2[_] for _ in keys)

            counter_temp = Counter(s[:k])
            for i in range(k, len_s + 1):
                if can_cover(counter_temp, counter_target):
                    return s[i - k:i]
                elif i == len_s:
                    return None
                counter_temp[s[i]] += 1
                counter_temp[s[i - k]] -= 1
            return None

        while lo <= hi:
            mid = (lo + hi) // 2
            var = validate(mid)
            if var:
                if res is None or len(res) > len(var):
                    res = var
                hi = mid - 1
            else:
                lo = mid + 1

        return res if res else ''


s = Solution()
assert s.minWindow(s="a", t="a") == "a"
assert s.minWindow(s="a", t="b") == ""
assert s.minWindow(s="aaaaaABCaDaaa", t="ABCD") == "ABCaD"
assert s.minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
