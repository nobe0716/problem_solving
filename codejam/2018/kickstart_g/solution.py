from collections import Counter


def count_triplet(n, nums):
    counters = [None for _ in range(len(nums))]
    c = Counter()
    for i in range(n):
        for j in range(i, n):
            if nums[i] not in c:
                c[nums[i]] = 0
        counters[i] = c

    r = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            a, b = nums[i], nums[j]
            current_counter = counters[j + 1]
            if a == 0 and b == 0:
                r += (n - j - 1)
            elif (a * b) in current_counter:
                r += current_counter[a * b]
            elif a == 0 or b == 0:
                continue
            elif a % b == 0 and (a // b) in current_counter:
                r += current_counter[a // b]
            elif b % a == 0 and (b // a) in current_counter:
                r += current_counter[b // a]
    return r


for test_cast_num in range(1, int(input()) + 1):
    n = int(input())
    nums = list(map(int, input().split()))

    r = count_triplet(n, nums)
    print("Case #%d: %d" % (test_cast_num, r))
