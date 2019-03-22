def get_good_count(n, s):
    if s[0] == '>' or s[-1] == '<':
        return 0
    c = 0
    l = 0
    while s[l] == '<':
        l += 1

    r = n - 1
    while s[r] == '>':
        r -= 1
    return min(l, n - r - 1)


for _ in range(int(input())):
    n = int(input())
    s = input()
    print(get_good_count(n, s))
