class Solution:
    def checkRecord(self, n: int) -> int:
        """
             00 01 02 10 11 12
              0  1  2  3  4  5 
        """
        now = [1, 0, 0, 0, 0, 0]
        VAL_X = 10 ** 9 + 7
        for i in range(1, n + 1):
            new = [
                    (now[0] + now[1] + now[2]) % VAL_X,
                    now[0],
                    now[1],
                    sum(now) % VAL_X,
                    now[3],
                    now[4]
                  ]
            now = new
        return sum(now) % VAL_X 
