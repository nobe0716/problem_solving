import sys
from functools import lru_cache

_MOD = 10 ** 9
sys.setrecursionlimit(100 * 10)


def solve(n):
    @lru_cache(None)
    def dp_with_history(i: int, cur_num: int, bit_mask: int):
        if i == 1:
            if cur_num != 0 and 2 ** cur_num == bit_mask:
                return 1
            return 0

        base = 2 ** cur_num
        c = 0
        if cur_num >= 1 and bit_mask & 2 ** (cur_num - 1) > 0:
            c += dp_with_history(i - 1, cur_num - 1, bit_mask ^ base) + dp_with_history(i - 1, cur_num - 1, bit_mask)
        if cur_num <= 8 and bit_mask & 2 ** (cur_num + 1) > 0:
            c += dp_with_history(i - 1, cur_num + 1, bit_mask ^ base) + dp_with_history(i - 1, cur_num + 1, bit_mask)
        return c

    ans = sum(dp_with_history(n, i, 1023) for i in range(10))
    # print(ans)
    return ans % _MOD


# 126461847755
# assert solve(11) == 3
# assert solve(10) == 1
# pre = sum(solve(i) for i in range(10, 41))
# print(pre)
# assert pre == 126_461_847_755
# print(solve(100))

n = int(input())
ans = solve(n)

print(ans)
