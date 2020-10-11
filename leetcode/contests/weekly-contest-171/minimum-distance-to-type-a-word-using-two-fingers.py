from functools import lru_cache
from string import ascii_uppercase


class Solution:
    def minimumDistance(self, word: str) -> int:
        grid = {k: (i // 6, i % 6) for i, k in enumerate(ascii_uppercase)}

        def dist(s, d):
            return abs(grid[s][0] - grid[d][0]) + abs(grid[s][1] - grid[d][1])

        word = ' ' + word
        n = len(word)
        ct = [[0] * n for _ in range(n)]
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                ct[j][i] = ct[i][j] = dist(word[i], word[j])

        @lru_cache(None)
        def dp(i: int, j: int, k: int) -> int:
            if k == n - 1:
                return 0
            return min(
                dp(k + 1, j, k + 1) + ct[i][k + 1],
                dp(i, k + 1, k + 1) + ct[j][k + 1]
            )

        return dp(0, 1, 1)


_DEBUG = False

_DEBUG = True

s = Solution()
assert s.minimumDistance(word="CAKE") == 3
assert s.minimumDistance(word="HAPPY") == 6
assert s.minimumDistance(word="NEW") == 3
assert s.minimumDistance(word="YEAR") == 7
assert s.minimumDistance(
    word="OPVUWZLCKTDPSUKGHAXIDWHLZFKNBDZEWHBSURTVCADUGTSDMCLDBTAGFWDPGXZBVARNTDICHCUJLNFBQOBTDWMGILXPSFWVGYBZVFFKQIDTOVFAPVNSQJULMVIERWAOXCKXBRI") == 295
assert s.minimumDistance(
    word="VGTCBCZIJRKDQHYFCNJJQESQUGRDNURMXYZIJOLSUEFDWDMMSOERVJLUPXNGPPWQKPUBOJEXPBTGALPMAQCVCVXVMALBDTAIUWJXHEYSJGDNOWKMFKNUVNEOWEQKEGFOLZMNZPMXHZGOGSWBMBHUCFLBXUVFHTJTCWQYJYLNOBUWQVURXNSOPIWPGKIBBBFLAJUA") == 386
assert s.minimumDistance(
    word="XTFMCZBADLXPKDVOLSWIVPZYHFRRCYQFAUFQNTVGOWVMIASEMFOSBMZCUSMKHQOBPTDIQPRUMPIFHRLFJTEOCCPMSNRCIPHDJELZDEVBVESRGABMRWYTPWWDPRLYKDVAHHPJIHAPLQKCCJSNHXLMYEHJGXYPVZLJMTEYDMLQPHUWLULNILMYYWJDPJDO")
assert s.minimumDistance(
    word="XTFMCZBADLXPKDVOLSWIVPZYHFRRCYQFAUFQNTVGOWVMIASEMFOSBMZCUSMKHQOBPTDIQPRUMPIFHRLFJTEOCCPMSNRCIPHDJELZDEVBVESRGABMRWYTPWWDPRLYKDVAHHPJIHAPLQKCCJSNHXLMYEHJGXYPVZLJMTEYDMLQPHUWLULNILMYYWJDPJDOXTFMCZBADLXPKDVOLSWIVPZYHFRRCYQFAUFQNTVGOWVMIASEMFOSBMZCUSMKHQOBPTDIQPRUMPIFHIQPRUMPIFHIQPRUMPIFHSDFS")
