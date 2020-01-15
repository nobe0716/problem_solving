import functools
import time
from string import ascii_uppercase


class Solution:
    def minimumDistance(self, word: str) -> int:
        MAX_VAL = 1000000
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
        act = [[0] * l for _ in range(l)]
        for i in range(l - 1):
            for j in range(i + 1, l):
                cost_ij = cost(i, j)
                ct[i][j] = ct[j][i] = cost_ij
                act[i][j] = act[i][j - 1] + cost(j - 1, j)

        if _DEBUG:
            print(time.time() - st)
            st = time.time()

        min_val = None

        @functools.lru_cache(maxsize=300 ** 3 * 2)
        def dp(i, j, finger):
            if i == 1:
                if finger == 0:
                    return act[0][j]
                else:
                    return MAX_VAL
            base = act[i][j]
            return min((dp(k, i - 1, 1 - finger) + ct[k - 1][i] + base) for k in range(1, i))

        min_val = min(
            min(dp(i, l - 1, 0) for i in range(1, l)),
            min(dp(i, l - 1, 1) for i in range(2, l))
        )
        if _DEBUG:
            print(time.time() - st)
            st = time.time()
        return min_val


_DEBUG = False

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
