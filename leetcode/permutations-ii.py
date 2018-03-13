from collections import Counter

class Solution(object):
    def back(self, s, l, cur, c):
        if len(cur) == l:
            s.add(tuple(cur))
            return
        for k in c.keys():
            c[k] -= 1
            if c[k] is 0:
                del c[k]
            cur.append(k)
            self.back(s, l, cur, c)
            cur.pop()
            if k not in c:
                c[k] = 1
            else:
                c[k] += 1

    def permuteUnique(self, nums):
        s = set()
        c = Counter(nums)
        self.back(s, len(nums), [], c)
        return list(map(list, s))