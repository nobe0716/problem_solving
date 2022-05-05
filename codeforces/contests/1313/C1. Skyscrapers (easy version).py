def proc(n, m):
    def calc(pivot):
        ans = [0] * n

        ans[pivot] = m[pivot]
        for i in range(pivot + 1, n):
            ans[i] = min(ans[i - 1], m[i])
        for i in range(pivot - 1, -1, -1):
            ans[i] = min(ans[i + 1], m[i])

        return sum(ans), ans

    max_sum = 0
    ans = None
    for i in range(n):
        v, r = calc(i)

        if v > max_sum:
            max_sum = v
            ans = r
    return ' '.join(map(str, ans))


n = int(input())
m = list(map(int, input().split()))

ans = proc(n, m)
print(ans)
