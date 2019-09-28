def solve(n, k, a):
    if k == 0:
        return a
    if k >= n:
        if n == 1:
            return '0'
        else:
            return '1' + '0' * (n - 1)
    a = list(a)
    if a[0] != '1':
        a[0] = '1'
        k -= 1
    for i in range(1, n):
        if k == 0:
            break
        if a[i] != '0':
            k -= 1
            a[i] = '0'
    return ''.join(a)


_DEBUG = False

if _DEBUG:
    assert solve(5, 3, '51528') == '10028'
    assert solve(3, 2, '102') == '100'
    assert solve(1, 1, '1') == '0'
n, k = map(int, input().split())
a = input()
print(solve(n, k, a))
