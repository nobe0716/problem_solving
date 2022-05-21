from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        original = [changed[0]]
        idx = 0
        for e in sorted(changed[1:]):
            if idx < len(original) and e == original[idx] * 2:
                idx += 1
                continue
            else:
                original.append(e)
        if len(original) != len(changed) // 2:
            return []
        return original


