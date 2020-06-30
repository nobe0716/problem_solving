from collections import Counter, defaultdict


def get_by(x):
    c = 0
    for i in range(n // 2):
        if x == a[i] + a[n - 1 - i]:
            continue
        if k + a[n - 1 - i] < x:
            c += 2
        else:
            c += 1
    return c


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    c = defaultdict(int)
    original_counter = Counter()
    one_diff_counter = Counter()
    for i in range(n // 2):
        x, y = a[i], a[n - i - 1]
        original_counter[x + y] += 1
        one_diff_counter[min(x, y) + 1] += 1
        one_diff_counter[max(x, y) + k + 1] -= 1

    one_diff = 0
    minimum_change = float('inf')
    for i in range(2, 2 * k + 1):
        zero_diff = original_counter[i]
        one_diff += one_diff_counter[i]
        two_diff = n - zero_diff - one_diff * 2
        change = one_diff + two_diff
        minimum_change = min(minimum_change, change)
    print(minimum_change)
