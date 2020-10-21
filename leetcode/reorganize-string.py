from collections import Counter
from itertools import chain


class Solution:
    def reorganizeString(self, S: str) -> str:
        c = Counter(S)
        order_by_occurrences = list(map(list, c.most_common()))
        most_common_counts = order_by_occurrences[0][1]
        len_of_s = len(S)
        if most_common_counts > len_of_s - most_common_counts + 1:
            return ''

        res = [None] * len_of_s
        j = 0
        for i in chain(range(0, len_of_s, 2), range(1, len_of_s, 2)):
            if order_by_occurrences[j][1] == 0:
                j += 1
            res[i] = order_by_occurrences[j][0]
            order_by_occurrences[j][1] -= 1
        return ''.join(res)


s = Solution()
print(s.reorganizeString('vvvlo'))
print(s.reorganizeString('ababaa'))
print(s.reorganizeString('aabbcc'))
print(s.reorganizeString('baa'))
