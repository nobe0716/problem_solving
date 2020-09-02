from typing import List, Tuple


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def embed(s: str) -> List[Tuple]:
            if not s:
                return []

            c = s[0]
            n = 1
            groups = []
            for e in s[1:]:
                if c == e:
                    n += 1
                else:
                    groups.append((c, n))
                    c = e
                    n = 1
            groups.append((c, n))
            return groups

        def applicable(src: List, dst: List) -> bool:
            # i = j = 0
            if len(src) != len(dst):
                return False
            for src_elem, dst_elem in zip(src, dst):
                if src_elem[0] != dst_elem[0]:
                    return False
                if src_elem[1] > dst_elem[1] or (src_elem[1] != dst_elem[1] and dst_elem[1] < 3):
                    return False
            return True

        embedded_s = embed(S)
        return sum(1 for _ in words if applicable(embed(_), embedded_s))


s = Solution()
assert s.expressiveWords(
    "dddiiiinnssssssoooo",
    ["dinnssoo", "ddinso", "ddiinnso", "ddiinnssoo", "ddiinso", "dinsoo", "ddiinsso", "dinssoo", "dinso"]) == 3
assert s.expressiveWords("aaa", ["aaaa"]) == 0
assert s.expressiveWords("zzzzzyyyyy", ["zzyy", "zy", "zyy"]) == 3
assert s.expressiveWords("heeellooo", ["hello", "hi", "helo"]) == 1
assert s.expressiveWords("heeeeeellooo", ["hello", "hi", "helo"]) == 1
assert s.expressiveWords("heeeeeellllllooo", ["hello", "hi", "helo"]) == 2
