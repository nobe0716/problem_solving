from collections import defaultdict


def backtrack(states, a, idx):
    if idx == 4:
        sum_dict = defaultdict(int)
        for state, ea in zip(states, a):
            sum_dict[state] += ea
        return sum_dict[True] == sum_dict[False]

    states[idx] = True
    if backtrack(states, a, idx + 1):
        return True
    states[idx] = False
    return backtrack(states, a, idx + 1)


def solve(a):
    a = sorted(a)
    return backtrack([False] * 4, a, 0)


assert solve([1, 7, 11, 5])
assert not solve([7, 3, 2, 5])
assert solve([3, 14, 36, 53])
a = list(map(int, input().split()))

print('YES' if solve(a) else 'NO')
