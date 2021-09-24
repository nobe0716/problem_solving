# https://codeforces.com/contest/1537/problem/E1


def solve(n, k, s):
    def compose(i):
        base = s[:i]
        return base * (k // len(base)) + base[:k % len(base)]

    ans = s[0] * k
    # s = list(s)
    for i in range(1, n + 1):
        composed = compose(i)
        ans = min(ans, composed)
    return ans


# assert solve(5, 10, 'dcdcd') == 'dcdcdcdcdc'
# assert solve(8, 16, 'dbcadabc') == 'dbcadabcdbcadabc'
n, k = map(int, input().strip().split())
s = input().strip()
# print(s)
ans = solve(n, k, s)
print(ans)

# dcdcddcdcd
# dcdcdcdcdc
