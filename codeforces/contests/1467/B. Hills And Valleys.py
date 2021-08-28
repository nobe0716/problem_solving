# https://codeforces.com/contest/1467/problem/B
import sys

input = sys.stdin.readline


def solve(n: int, a):
    def hill_or_valley(i: int) -> int:
        if i == 0 or i == n - 1:
            return 0
        if (a[i - 1] < a[i] and a[i] > a[i + 1]) or (a[i - 1] > a[i] and a[i] < a[i + 1]):
            return 1
        return 0

    t = [0] * n
    for i in range(1, n - 1):
        t[i] = hill_or_valley(i)
    ans = ans_origin = sum(t)

    for i in range(1, n - 1):
        tmp = a[i]

        a[i] = a[i - 1]
        ans = min(ans, ans_origin - sum(t[i - 1:i + 2]) + sum(hill_or_valley(i) for i in range(i - 1, i + 2)))
        a[i] = a[i + 1]
        ans = min(ans, ans_origin - sum(t[i - 1:i + 2]) + sum(hill_or_valley(i) for i in range(i - 1, i + 2)))

        a[i] = tmp

        if ans_origin - ans == 3:
            return ans

    # print(ans)
    return ans


# assert solve(6, [int(x) for x in '1 6 2 5 2 10'.split()]) == 1
# assert solve(5, [1, 6, 2, 5, 1]) == 0
# assert solve(6, [1, 2, 1, 1, 2, 1]) == 1

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip().split()))
    r = solve(n, a)
    print(r)
