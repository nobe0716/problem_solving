from string import ascii_lowercase


def solve(n: int, p: int, s: str) -> int:
    if s == s[::-1]:
        return 0

    def get_dist(src: str, dsc: str) -> int:
        src_idx, dsc_idx = ascii_lowercase.index(src), ascii_lowercase.index(dsc)
        if src_idx > dsc_idx:
            src_idx, dsc_idx = dsc_idx, src_idx
        return min(dsc_idx - src_idx, src_idx + 26 - dsc_idx)

    p -= 1
    is_palindromic = [False] * n
    up_down_cost = 0
    for i in range((n + 1) // 2):
        if s[i] == s[n - i - 1]:
            is_palindromic[i] = is_palindromic[n - i - 1] = True
        else:
            up_down_cost += get_dist(s[i], s[n - i - 1])

    idx_of_not_palindromic = list(i for i in range(n) if not is_palindromic[i])
    if p < n // 2:
        idx_of_not_palindromic = list(_ for _ in idx_of_not_palindromic if _ < (n + 1) // 2)
    else:
        idx_of_not_palindromic = list(_ for _ in idx_of_not_palindromic if _ >= (n + 1) // 2)

    move_cost_candidates = []
    min_idx, max_idx = min(idx_of_not_palindromic), max(idx_of_not_palindromic)
    if p < min_idx:
        move_cost_candidates.append(max_idx - p)
    if p > max_idx:
        move_cost_candidates.append(p - min_idx)
    move_cost_candidates.append(max_idx - min_idx + min(abs(p - max_idx), abs(p - min_idx)))
    return up_down_cost + min(move_cost_candidates)


# assert solve(8, 3, 'aeabcaez') == 6
# assert solve(8, 3, 'abcddcbb') == 3
# assert solve(4, 4, 'rkoa') == 14
# assert solve(39, 30, 'yehuqwaffoiyxhkmdipxroolhahbhzprioobxfy') == 138
n, p = map(int, input().split())
s = input()
print(solve(n, p, s))
