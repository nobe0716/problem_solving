from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        s = [arr[0]]
        for e in arr[1:]:
            s.append(s[-1] ^ e)
        result = []
        for l, r in queries:
            if l == 0:
                result.append(s[r])
            else:
                result.append(s[r] ^ s[l - 1])
        return result


s = Solution()
print(s.xorQueries(arr=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [0, 3], [3, 3]]))
print(s.xorQueries(arr=[4, 8, 2, 10], queries=[[2, 3], [1, 3], [0, 0], [0, 3]]))
