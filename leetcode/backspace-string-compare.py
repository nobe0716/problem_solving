class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def get_new_pos(p: int, s: str) -> int:
            sc = 0
            while p >= 0 and (sc > 0 or s[p] == '#'):
                if s[p] == '#':
                    sc += 1
                else:
                    sc -= 1
                p -= 1
            return p

        index_s, index_t = len(S) - 1, len(T) - 1

        while index_s >= 0 and index_t >= 0:
            index_s = get_new_pos(index_s, S)
            index_t = get_new_pos(index_t, T)
            if index_s < 0 and index_t < 0:
                return True
            elif index_s < 0 or index_t < 0 or S[index_s] != T[index_t]:
                return False
            index_s -= 1
            index_t -= 1

        index_s = get_new_pos(index_s, S)
        index_t = get_new_pos(index_t, T)
        return index_s < 0 and index_t < 0
