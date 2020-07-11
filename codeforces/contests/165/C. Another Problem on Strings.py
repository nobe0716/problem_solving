def solve(k, s):
    c = 0
    zeros = map(len, s.split('1'))
    if k > 0:
        zeros = list(zeros)
        l = len(zeros)
        # print(zeros)
        for i in range(l - k + 1):
            if i + k >= l:
                continue
            head, tail = zeros[i], zeros[i + k]
            c += (head + 1) * (tail + 1)
        return c
    else:  # k == 0
        return sum(e * (e + 1) // 2 for e in zeros)


k = int(input())
s = input()
print(solve(k, s))
