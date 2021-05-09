def solve(n):
    nums = [6, 10, 15]

    used = set(nums)
    base = [6, 10, 15]
    count = [1, 1, 1]
    for _ in range(n - len(nums)):
        next_num_candidates = []
        for i in range(3):
            while base[i] * count[i] in used:
                count[i] += 1
            next_num_candidates.append((base[i] * count[i], i))

        next_num_candidates.sort()
        new_num, new_idx = next_num_candidates[0]
        nums.append(new_num)
        used.add(new_num)
        count[new_idx] += 1

    return nums


n = int(input())
res = solve(n)
print(' '.join(map(str, res)))
