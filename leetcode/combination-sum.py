class Solution(object):
    def combinationSum(self, candidates, target):
        def helper(candidates, target, cur, res):
            if target == 0:
                res.append(list(cur))
                return None
            if len(candidates) == 0:
                return None
            c = candidates[0]
            i = 0
            while target >= c * i:
                helper(candidates[1:], target - c * i, cur + [c] * i, res)
                i += 1

        res = []
        helper(candidates, target, [], res)
        return res
