import sys

sys.setrecursionlimit(10000)


class Solution(object):
    def catMouseGame(self, g):
        def pr(c, m, t):
            k = (c, m, t)
            if k in d:
                return d[k]
            d[k] = 0
            if t:
                if 0 in g[m]:
                    d[k] = 1
                    return 1
                r = 2
                for n in g[m]:
                    if n == c:
                        continue
                    v = pr(c, n, False)
                    if v == 1:
                        r = 1
                        break
                    elif v == 0:
                        r = 0
            else:
                if m in g[c]:
                    d[k] = 2
                    return 2
                r = 1
                for n in g[c]:
                    if n == 0:
                        continue
                    v = pr(n, m, True)
                    if v == 2:
                        r = 2
                        break
                    elif v == 0:
                        r = 0
            d[k] = r
            return r

        d = {}

        return pr(2, 1, True)


s = Solution()
# print(s.catMouseGame([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]))
# print(s.catMouseGame([[2, 3], [3, 4], [0, 4], [0, 1], [1, 2]]))
# print(s.catMouseGame([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]))
print(s.catMouseGame([[6], [4], [9], [5], [1, 5], [3, 4, 6], [0, 5, 10], [8, 9, 10], [7], [2, 7], [6, 7]]))
