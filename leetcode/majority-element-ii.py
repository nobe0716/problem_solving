class Solution(object):
    def majorityElement(self, nums):
        l = len(nums)
        if l == 1:
            return nums
        v = l // 3

        e1 = e2 = c1 = c2 = 0
        for e in nums:
            if e1 == e:
                c1 += 1
                continue
            elif e2 == e:
                c2 += 1
                continue

            if c1 == 0 and e != e2:
                e1, c1 = e, 1
                continue
            elif c2 == 0 and e != e1:
                e2, c2 = e, 1
                continue

            if c1 > 0 and e != e1:
                c1 -= 1
            if c2 > 0 and e != e2:
                c2 -= 1

        c1 = c2 = 0
        for e in nums:
            c1 += 1 if e == e1 else 0
            c2 += 1 if e == e2 else 0
        r = []
        if c1 > l // 3:
            r.append(e1)
        if c2 > l // 3 and e2 not in r:
            r.append(e2)
        return r
