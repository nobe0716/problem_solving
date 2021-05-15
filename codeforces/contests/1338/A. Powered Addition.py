def solve(n, a):
    current_max_num = a[0]
    current_time_elapsed = 0
    for i in range(1, n):
        if a[i] >= current_max_num:
            current_max_num = a[i]
            continue

        j = 0
        while a[i] + 2 ** j - 1 < current_max_num:
            # a[i] += 2 ** j
            j += 1

        current_time_elapsed = max(current_time_elapsed, j)
        # current_max_num = max(current_max_num, a[i])
    # print(current_time_elapsed)
    return current_time_elapsed


assert solve(4, [1, 7, 6, 5]) == 2
assert solve(5, [1, 2, 3, 4, 5]) == 0
assert solve(2, [0, -4]) == 3
assert solve(4, [2, -1, -3, -4]) == 3

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    res = solve(n, a)
    print(res)
