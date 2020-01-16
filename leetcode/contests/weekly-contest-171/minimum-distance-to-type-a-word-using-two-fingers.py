import functools
import time
from string import ascii_uppercase


class Solution:
    def minimumDistance(self, word: str) -> int:
        COL_SIZE = 6
        word = ' ' + word
        l = len(word)
        g = {ch: (i // COL_SIZE, i % COL_SIZE) for i, ch in enumerate(ascii_uppercase)}
        st = time.time()

        def cost(src, dst):
            if src == 0 or dst == 0:
                return 0
            sw = word[src]
            dw = word[dst]
            return abs(g[sw][0] - g[dw][0]) + abs(g[sw][1] - g[dw][1])

        ct = [[0] * l for _ in range(l)]
        for i in range(l - 1):
            for j in range(i + 1, l):
                cost_ij = cost(i, j)
                ct[i][j] = ct[j][i] = cost_ij

        @functools.lru_cache(None)
        def dp(i, j, k):
            if i == l - 1 or j == l - 1:
                return 0
            return min(
                dp(k + 1, j, k + 1) + ct[i][k + 1],
                dp(i, k + 1, k + 1) + ct[j][k + 1])

        min_val = dp(1, 0, 1)
        if _DEBUG:
            print('len({}), min_val: {}, elapsed: {}'.format(len(word) - 1, min_val, time.time() - st))
            st = time.time()

        return min_val


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
