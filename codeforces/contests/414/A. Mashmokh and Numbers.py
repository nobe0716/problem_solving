# 2022-05-15T00:50:46.010Z


def proc(n, k):
    if n == 1:
        return [1] if k == 0 else [-1]
    if n // 2 > k:
        return [-1]

    num_of_pairs = n // 2

    k -= (num_of_pairs - 1)

    ans = [k, 2 * k]
    base = 2 * k + 1
    for i in range(n - 2):
        ans.append(base)
        base += 1
    return ans


n, k = map(int, input().split())
ans = proc(n, k)
print(' '.join(map(str, ans)))
