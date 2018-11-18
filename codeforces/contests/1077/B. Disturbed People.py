n = int(input())
m = list(map(int, input().split()))
is_disturbed = [(0 < i < n - 1 and m[i - 1] == m[i + 1] == 1 and m[i] == 0) for i in range(n)]
# print(is_disturbed)
c = 0
while any(is_disturbed):
    happened = False
    for i in range(1, n - 1):
        if is_disturbed[i - 1] and is_disturbed[i + 1]:
            m[i] = 0
            is_disturbed[i - 1] = is_disturbed[i + 1] = False
            happened = True
            break
    if not happened:
        for i in range(0, n - 1):
            if is_disturbed[i + 1]:
                m[i] = 0
                is_disturbed[i + 1] = False
                break
    c += 1
print(c)
# print(m)
# print(is_disturbed)
