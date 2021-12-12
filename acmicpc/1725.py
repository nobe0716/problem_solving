import sys

input = sys.stdin.readline


def solve(n, a):
    stack = []
    ans = 0
    for i, e in enumerate(a):
        while stack and stack[-1][2] >= e:
            lo, hi, v = stack.pop()
            ans = max(ans, (i - lo) * v)

        if stack:
            stack.append((stack[-1][1] + 1, i, e))
        else:
            stack.append((0, i, e))

    while stack:
        lo, hi, v = stack.pop()
        ans = max(ans, (n - lo) * v)

    return ans


n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

print(solve(n, a))
