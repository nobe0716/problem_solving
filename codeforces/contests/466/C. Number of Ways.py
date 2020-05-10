# sys.stdin = open('c.in')

n = int(input())
a = map(int, input().split())

v = 0
s = []
for e in a:
    v += e
    s.append(v)

total_sum = s[-1]

if total_sum % 3 != 0:
    print(0)
else:
    # l_idx = [0]
    r_idx = [0] * n
    for i in range(n - 1, 0, -1):
        if i < n - 1:
            r_idx[i] = r_idx[i + 1]
        if s[i - 1] == (total_sum // 3 * 2):
            r_idx[i] += 1
    # print(r_idx)
    r = 0
    for i in range(n - 2):
        if s[i] == total_sum // 3:
            r += r_idx[i + 2]
    print(r)
