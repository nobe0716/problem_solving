def solve(n):
    if n % 2 == 0:
        return None
    a = [None] * 2 * n

    even_p, odd_p = 0, n + 1
    for i in range(n):
        current_num = i * 2 + 1
        if i % 2 == 0:
            a[even_p], a[even_p + n] = current_num, current_num + 1
            even_p += 2
        else:
            a[odd_p], a[odd_p - n] = current_num, current_num + 1
            odd_p += 2
    return a


n = int(input())
a = solve(n)
if not a:
    print('NO')
else:
    print('YES')
    print(' '.join(map(str, a)))

# b = [0] * 2 * n
# for i in range(2 * n):
#     for j in range(i, i + n):
#         b[i] += a[j % (2 * n)]
# print(' '.join(map(str, b)))
