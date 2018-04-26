from collections import Counter

class Solution(object):
    def comb(self, c, l, i):
        if i == len(c.keys()):
            return l

        r = l.copy()
        new_num = list(c.keys())[i]
        for e in l:
            for j in range(1, c[new_num] + 1):
                e_l = list(e)
                for k in range(j):
                    e_l.append(new_num)
                r.append(e_l)

        return self.comb(c, r, i + 1)


    def subsetsWithDup(self, nums):
        c = Counter(nums)
        return self.comb(c, [[]], 0)


s = Solution()
print (s.subsetsWithDup([1,2,2]))
