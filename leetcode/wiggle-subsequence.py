class Solution(object):
    def wiggleMaxLength(self, nums):
        s = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        n = [0 for i in range(len(s))]
        p = [0 for i in range(len(s))]
        t = [0 for i in range(len(s))]
        for i in range(0, len(s)):
            if s[i] > 0:
                p[i] = n[i - 1] + 1
                n[i] = 1
            elif s[i] < 0:
                p[i] = 1
                n[i] = p[i - 1] + 1
            else:
                p[i] = 0
                p[i] = 0
            t[i] = max([p[i], n[i]])
        print(s)
        print(n)
        print(p)
        print(t)
        print(max(t) + 1)
        print("=============================")
        return max(t) + 1


s = Solution()
s.wiggleMaxLength([1,7,4,9,2,5])
s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
s.wiggleMaxLength([1,2,3,4,5,6,7,8,9])
# assert(s.wiggleMaxLength([1,7,4,9,2,5]) == 6)
# assert(s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]) == 7)
# assert(s.wiggleMaxLength([1,2,3,4,5,6,7,8,9]) == 2)
