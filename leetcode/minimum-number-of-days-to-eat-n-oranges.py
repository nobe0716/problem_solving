class Solution:

    def minDays(self, n: int) -> int:
        r = 0
        q = {n}
        v = set()
        while q:
            nq = set()
            v.update(q)
            for e in q:
                if e == 1:
                    return r + 1
                if e % 3 == 0 and (e // 3) not in v:
                    nq.add(e // 3)
                if e % 2 == 0 and (e // 2) not in v:
                    nq.add(e // 2)
                if (e - 1) not in v:
                    nq.add(e - 1)
            r += 1
            q = nq

        return -1


s = Solution()
assert s.minDays(10) == 4
# assert s.minDays(1541786975) == 1
assert s.minDays(1684352734) == 33
# assert s.minDays(2 * 10 ** 9) == 32
