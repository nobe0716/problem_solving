# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
from collections import Counter
from typing import List

SECRET = 'hbaczn'


class Master:
    def guess(self, word: str) -> int:
        return sum(1 for i in range(6) if word[i] == SECRET[i])


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def countMatches(a, b):
            return sum(1 for i in range(6) if a[i] == b[i])

        n = len(wordlist)
        match_counts = [[0] * n for _ in range(n)]

        for i in range(n - 1):
            for j in range(i + 1, n):
                match_counts[i][j] = match_counts[j][i] = countMatches(wordlist[i], wordlist[j])

        # counters =
        candidates = []
        for i in range(n):
            c = Counter(match_counts[i])
            e = [c[j] for j in range(6, -1, -1)] + [wordlist[i], i]
            candidates.append(e)

        candidates.sort(reverse=True)
        while len(candidates) > 1:
            e = candidates[0]
            w = e[7]
            i = e[8]

            match_count = master.guess(w)
            if match_count == 6:
                return

            new_candidates = []
            for candidate in candidates:
                if candidate[7] == w:
                    continue
                if match_counts[i][candidate[8]] == match_count:
                    new_candidates.append(candidate)

            candidates = sorted(new_candidates, reverse=True)

        master.guess(candidates[0][7])


m = Master()
s = Solution()

SECRET = "hbaczn"
s.findSecretWord(["gaxckt", "trlccr", "jxwhkz", "ycbfps", "peayuf", "yiejjw", "ldzccp", "nqsjoa", "qrjasy", "pcldos",
                  "acrtag", "buyeia", "ubmtpj", "drtclz", "zqderp", "snywek", "caoztp", "ibpghw", "evtkhl", "bhpfla",
                  "ymqhxk", "qkvipb", "tvmued", "rvbass", "axeasm", "qolsjg", "roswcb", "vdjgxx", "bugbyv", "zipjpc",
                  "tamszl", "osdifo", "dvxlxm", "iwmyfb", "wmnwhe", "hslnop", "nkrfwn", "puvgve", "rqsqpq", "jwoswl",
                  "tittgf", "evqsqe", "aishiv", "pmwovj", "sorbte", "hbaczn", "coifed", "hrctvp", "vkytbw", "dizcxz",
                  "arabol", "uywurk", "ppywdo", "resfls", "tmoliy", "etriev", "oanvlx", "wcsnzy", "loufkw", "onnwcy",
                  "novblw", "mtxgwe", "rgrdbt", "ckolob", "kxnflb", "phonmg", "egcdab", "cykndr", "lkzobv", "ifwmwp",
                  "jqmbib", "mypnvf", "lnrgnj", "clijwa", "kiioqr", "syzebr", "rqsmhg", "sczjmz", "hsdjfp", "mjcgvm",
                  "ajotcx", "olgnfv", "mjyjxj", "wzgbmg", "lpcnbj", "yjjlwn", "blrogv", "bdplzs", "oxblph", "twejel",
                  "rupapy", "euwrrz", "apiqzu", "ydcroj", "ldvzgq", "zailgu", "xgqpsr", "wxdyho", "alrplq", "brklfk"],
                 m)
SECRET = "acckzz"
s.findSecretWord(["ccbazz", "eiowzz", "abcczz", "acckzz"], m)
