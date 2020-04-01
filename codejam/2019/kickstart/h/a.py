# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edd/00000000001a274e
from collections import Counter


def solve(n, a):
    h_indice = []
    h_index = 0
    count = 0
    counter = Counter()
    for i in range(n):
        v = a[i]
        if v <= h_index:
            h_indice.append(h_index)
            continue

        counter[v] += 1
        count += 1

        while h_index + 1 <= count:
            h_index += 1
            if counter[h_index] > 0:
                count -= counter[h_index]
        h_indice.append(h_index)
    return ' '.join(map(str, h_indice))


for test_num in range(1, int(input()) + 1):
    n = int(input())
    a = list(map(int, input().split()))
    r = solve(n, a)
    print('Case #{}: {}'.format(test_num, r))
