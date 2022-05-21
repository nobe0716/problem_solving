from typing import List


class Solution:
    # 3 min - brute force
    # def differByOne(self, dict: List[str]) -> bool:
    #     def countDiff(alpha: str, beta: str) -> int:
    #         return sum(0 if a == b else 1 for a, b in zip(alpha, beta))
    #
    #     return any(countDiff(a, b) == 1 for a, b in combinations(dict, 2))

    def differByOne(self, dict: List[str]) -> bool:
        for i in range(len(dict[0])):
            word_set = set()
            for s in dict:
                word = s[:i] + s[i + 1:]
                if word in word_set:
                    return True
                word_set.add(word)
        return False

s = Solution()
assert s.differByOne(["debd","debc"])