from collections import defaultdict

num_of_test = int(input())
for test_num in range(1, num_of_test + 1):
    n = int(input())
    a = list(map(int, input().split()))
    a = list(sorted(a, reverse=True))

    res = 0
    count_dict = defaultdict(int)
    for i in range(0, n):
        if a[i] > 0:
            for j in range(i + 1, n):
                if a[j] == 0:
                    continue
                res += count_dict[a[i] * a[j]]
        # if a[i] == 0:
        #     break
        count_dict[a[i]] += 1

    zero_cnt = count_dict[0]
    if zero_cnt >= 3:
        res += (zero_cnt * (zero_cnt - 1) * (zero_cnt - 2) // 6)
    if zero_cnt >= 2:
        res += (zero_cnt * (zero_cnt - 1) // 2 * (n - zero_cnt))
    print('Case #{}: {}'.format(test_num, res))
    # brute_force_res = 0
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         for k in range(j + 1, n):
    #             if a[i] == a[j] * a[k] or a[j] == a[i] * a[k] or a[k] == a[i] * a[j]:
    #                 brute_force_res += 1
    #
    # if res != brute_force_res:
    #     print('wtf')
