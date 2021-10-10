# https://codeforces.com/problemset/problem/1486/B
import sys

_DEBUG = False
if not _DEBUG:
    input = sys.stdin.readline


def solve(n, houses):
    def solve_sub_prob(n, pos):
        pos = sorted(pos)
        return pos[n // 2] - pos[(n - 1) // 2] + 1

    pos_x = []
    pos_y = []
    for x, y in houses:
        pos_x.append(x)
        pos_y.append(y)

    by_x = solve_sub_prob(n, pos_x)
    by_y = solve_sub_prob(n, pos_y)
    ans = by_x * by_y
    return ans


# assert solve(3, [[0, 0], [2, 0], [1, 2]]) == 1
# assert solve(4, [[1, 0], [0, 2], [2, 3], [3, 1]]) == 4
# assert solve(4, [[0, 0], [0, 1], [1, 0], [1, 1]]) == 4
# assert solve(2, [[0, 0], [1, 1]]) == 4
# assert solve(2, [[0, 0], [2, 0]]) == 3
# assert solve(2, [[0, 0], [0, 0]]) == 1
# assert solve(8, [[756764518, 412103839], [722460568, 195282969], [979780191, 450793610], [492197753, 953546232], [2676986, 367487969], [48946904, 641467344], [532147443, 443507707], [794863955, 592048652]]) == 1386603165975904

for _ in range(int(input())):
    n = int(input())
    houses = []
    for _ in range(n):
        x, y = map(int, input().strip().split())
        houses.append((x, y))
    ans = solve(n, houses)
    print(ans)
