# https://codeforces.com/contest/1554/problem/B
import sys

input = sys.stdin.buffer.readline


def solve(n, k, a):
    ans = float('-inf')
    for i in range(max(0, n - 2 * k - 1), n - 1):
        for j in range(i + 1, n):
            ans = max(ans, (i + 1) * (j + 1) - k * (a[i] | a[j]))
    return ans


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().strip().split()))
    ans = solve(n, k, a)
    print(ans)
