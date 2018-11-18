def count_triplet(n, nums):
    r = 0
    for i in range(n - 2):

        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] * nums[j] == nums[k] or nums[j] * nums[k] == nums[i] or nums[k] * nums[i] == nums[j]:
                    r += 1
    return r


for test_cast_num in range(1, int(input()) + 1):
    n = int(input())
    nums = list(map(int, input().split()))

    r = count_triplet(n, nums)
    print("Case #%d: %d" % (test_cast_num, r))
