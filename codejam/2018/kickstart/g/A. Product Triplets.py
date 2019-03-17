from collections import defaultdict

num_of_test = int(input())
for test_num in range(1, num_of_test + 1):
    n = int(input())
    a = list(map(int, input().split()))
    a = list(sorted(a, reverse=True))
    res = 0
    count_dict = defaultdict(int)

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            res += count_dict[a[i] * a[j]]
        count_dict[a[i]] += 1

    print('Case #{}: {}'.format(test_num, res))
