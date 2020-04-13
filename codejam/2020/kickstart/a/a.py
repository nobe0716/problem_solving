# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56

for t in range(1, int(input()) + 1):
    n, b = map(int, input().split())
    a = map(int, input().split())
    a = sorted(a)
    c = 0
    for cost in a:
        if b < cost:
            break
        b -= cost
        c += 1
    print('Case #{}: {}'.format(t, c))
