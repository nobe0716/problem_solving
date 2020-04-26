class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r = 0
        # if len(text1) > len(text2):
        #     text1, text2 = text2, text1
        t = [[0] * len(text2) for _ in range(len(text1))]
        r = 0
        for i in range(len(text1)):
            for j in range(len(text2)):
                if i == 0 or j == 0:
                    t[i][j] = 1 if text1[i] == text2[j] else 0
                    if i > 0:
                        t[i][j] = max(t[i][j], t[i - 1][j])
                    if j > 0:
                        t[i][j] = max(t[i][j], t[i][j - 1])
                else:
                    t[i][j] = t[i - 1][j - 1] + (1 if text1[i] == text2[j] else 0)
                    t[i][j] = max(t[i][j], t[i - 1][j], t[i][j - 1])
                r = max(r, t[i][j])
            # print(' '.join(map(str, t[i])))
        return r
