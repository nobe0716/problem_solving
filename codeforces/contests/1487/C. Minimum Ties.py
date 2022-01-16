# https://codeforces.com/problemset/problem/1487/C
import itertools
import sys

_DEBUG = True
if not _DEBUG:
    input = sys.stdin.readline


def solve(n):
    num_games = n * (n - 1) // 2
    for i in range(num_games + 1):  # i - num of ties
        total_score = 2 * i + (num_games - i) * 3
        if total_score % n != 0:
            continue
        score_per_team = total_score // n
        scores = [0] * n
        result = []
        for a, b in itertools.combinations(range(n), 2):
            if scores[a] + 3 <= score_per_team:
                scores[a] += 3
                result.append(1)
            elif scores[a] == score_per_team:
                scores[b] += 3
                result.append(-1)
            else:
                scores[a] += 1
                scores[b] += 1
                result.append(0)
        return result
    return None


for _ in range(int(input())):
    n = int(input())
    ans = solve(n)
    print(' '.join(map(str, ans)))
