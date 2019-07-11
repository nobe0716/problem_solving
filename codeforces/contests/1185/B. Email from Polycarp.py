def is_printable(a, b):
    if a[0] != b[0]:
        return False
    m, n = len(a), len(b)
    i = j = 0

    while i < m and j < n:
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            while j < n and a[i] != b[j]:
                if a[i - 1] != b[j]:
                    return False
                j += 1
    while j < n and a[i - 1] == b[j]:
        j += 1

    return i == m and j == n


t = int(input())
for _ in range(t):
    a, b = input(), input()
    print('YES' if is_printable(a, b) else 'NO')
