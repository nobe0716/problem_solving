num_of_tests = int(input())
for test_num in range(1, num_of_tests + 1):
    n = int(input())
    scores = list(map(int, list(input())))
    t = [0] * n
    k = (n + 1) // 2
    t[0] = sum(scores[:k])
    for i in range(1, n - k + 1):
        t[i] = t[i - 1] - scores[i - 1] + scores[i + k - 1]
    print('Case #{}: {}'.format(test_num, max(t)))
