from collections import Counter


class Solution(object):
    def combinationSum2(self, candidates, target):
        def helper(c, keys, target, cur, res):
            # print(c, keys, target, cur, res)
            if target == 0:
                res.append(list(cur))
                return None
            if len(keys) == 0:
                return None
            k = keys[0]
            v = c[k]
            i = 0
            for i in range(v + 1):
                if k * i > target:
                    continue
                helper(c, keys[1:], target - k * i, cur + [k] * i, res)

        c = Counter(candidates)
        res = []
        helper(c, list(sorted(c.keys())), target, [], res)
        return res
