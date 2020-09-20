_MODER = 10 ** 9 + 7


class Solution:
    def checkRecord(self, n: int) -> int:
        """
        t[0]: 0-A, 0-continous-L
        t[1]: 0-A, 1-continous-L
        t[2]: 0-A, 2-continous-L
        t[3]: 1-A, 0-continous-L
        t[4]: 1-A, 1-continous-L
        t[5]: 1-A, 2-continous-L

        initial t = [1, 0, 0, 0, 0, 0]

        new one can be one of `ALP`

        new t[0] = t[0] + t[1] + t[2] (append 'P')
        new t[1] = t[0] (append 'L')
        new t[2] = t[1] (append 'L')
        new t[3] = t[0] + t[1] + t[2] (append 'A') + t[3] + t[4] + t[5] (append 'P')
        new t[4] = t[3] (append 'L')
        new t[5] = t[4] (append 'L')
        """
        t = [1] + [0] * 5
        for i in range(n):
            t = [
                sum(t[0:3]) % _MODER,
                t[0],
                t[1],
                sum(t) % _MODER,
                t[3],
                t[4],
            ]
        return sum(t) % _MODER


s = Solution()
assert s.checkRecord(2) == 8
