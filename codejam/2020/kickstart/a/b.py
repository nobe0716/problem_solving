# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d40bb
import functools


def solve(n, k, p, plates):
    @functools.lru_cache(None)
    def dp(start_idx, end_idx, total_plate):
        if total_plate >= (end_idx - start_idx) * k:
            return sum(plates[i][k] for i in range(start_idx, end_idx))
        if end_idx - start_idx <= 1:
            return plates[start_idx][total_plate]
        idx = (start_idx + end_idx) // 2
        r = 0
        for i in range(0, total_plate + 1):
            j = total_plate - i
            r = max(r, dp(start_idx, idx, i) + dp(idx, end_idx, j))
        # print(start_idx, end_idx, total_plate, '==>', r)
        return r

    for i in range(n):
        for j in range(1, k):
            plates[i][j] += plates[i][j - 1]
        plates[i] = [0] + plates[i]
    return dp(0, n, p)


for t in range(1, int(input()) + 1):
    n, k, p = map(int, input().split())
    plates = [list(map(int, input().split())) for _ in range(n)]
    r = solve(n, k, p, plates)
    print('Case #{}: {}'.format(t, r))
