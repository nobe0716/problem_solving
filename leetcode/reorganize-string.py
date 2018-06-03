import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, S):
        l = len(S)
        if l <= 1:
            return S
        c = Counter(S)
        h = [(c[k], k) for k in c]
        heapq._heapify_max(h)
        # print(h)

        r = [None] * l
        v, k = heapq._heappop_max(h)
        if v > (l + 1) // 2:
            return ""

        if v > 1:
            heapq.heappush(h, (v - 1, k))
        r[0] = k
        i = 1

        for _ in range(l - 1):
            v, k = heapq._heappop_max(h)
            # if r[i - 1] == k:
            #     i += 1
            while r[i] is not None or r[i - 1] == k:
                i += 1
                if i >= l:
                    i = 1
            r[i] = k
            v -= 1
            # append it again when it is not 0
            if v > 0:
                heapq.heappush(h, (v, k))
        return ''.join(r)


s = Solution()
print(s.reorganizeString('vvvlo'))
print(s.reorganizeString('ababaa'))
print(s.reorganizeString('aabbcc'))
print(s.reorganizeString('baa'))
